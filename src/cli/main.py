"""CLI entry point — typer-based.

Commands:
  generate  — Single adversarial prompt generation
  campaign  — Continuous fuzzing campaign
  evaluate  — Evaluate a prompt against a target
  report    — Generate assessment report
  export    — Export archive to promptfoo or JSON format
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from src import GenerationConfig
from src.narrative_engine.generator import NarrativeEngine

app = typer.Typer(
    name="narrative-engine",
    help="Narrative Engine v3.0 — Adversarial prompt generation engine.",
    no_args_is_help=True,
)
console = Console()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _build_config(
    target_model: str = "gpt-4o",
    target_url: str = "https://api.openai.com/v1",
    attacker_model: str = "gpt-4o",
    attacker_url: str = "https://api.openai.com/v1",
    judge_model: str = "gpt-4o",
    judge_url: str = "https://api.openai.com/v1",
    concurrency: int = 32,
    iterations: int = 1000,
    seed_dir: str = "prompts/seeds",
) -> GenerationConfig:
    """Build a GenerationConfig from CLI parameters."""
    return GenerationConfig(
        target_model=target_model,
        target_base_url=target_url,
        attacker_model=attacker_model,
        attacker_base_url=attacker_url,
        judge_model=judge_model,
        judge_base_url=judge_url,
        concurrency=concurrency,
        n_iterations=iterations,
        seed_dir=seed_dir,
    )


def _run_async(coro):  # type: ignore[no-untyped-def]
    """Run an async coroutine in a new event loop."""
    return asyncio.run(coro)


def _load_questions(path: str) -> list[str]:
    """Load questions from a file (one per line or JSON array)."""
    p = Path(path)
    if not p.exists():
        console.print(f"[red]Questions file not found: {path}[/red]")
        raise typer.Exit(1)

    text = p.read_text(encoding="utf-8").strip()
    if text.startswith("["):
        data = json.loads(text)
        if isinstance(data, list):
            return [str(q) for q in data if q]
    return [line.strip() for line in text.splitlines() if line.strip()]


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

@app.command()
def generate(
    question: str = typer.Argument(..., help="The test objective / harmful behaviour."),
    target_model: str = typer.Option("gpt-4o", "--target", "-t", help="Target model name."),
    target_url: str = typer.Option(
        "https://api.openai.com/v1", "--target-url", help="Target API base URL."
    ),
    attacker_model: str = typer.Option("gpt-4o", "--attacker", "-a", help="Attacker model."),
    attacker_url: str = typer.Option(
        "https://api.openai.com/v1", "--attacker-url", help="Attacker API base URL."
    ),
    budget: str = typer.Option("medium", "--budget", "-b", help="Eval budget: fast|medium|full."),
    seed_dir: str = typer.Option("prompts/seeds", "--seeds", help="Seed template directory."),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (JSON)."),
) -> None:
    """Generate a single adversarial prompt for a given objective."""
    config = _build_config(
        target_model=target_model,
        target_url=target_url,
        attacker_model=attacker_model,
        attacker_url=attacker_url,
        seed_dir=seed_dir,
    )

    async def run() -> dict:
        engine = NarrativeEngine(config)
        await engine.initialize()
        try:
            result = await engine.generate_single(question, budget=budget)
            return result
        finally:
            await engine.shutdown()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        progress.add_task("Generating adversarial prompt...", total=None)
        result = _run_async(run())

    # Display result
    jb_status = "[green]JAILBREAK[/green]" if result["is_jailbreak"] else "[red]BLOCKED[/red]"
    console.print(Panel(
        f"[bold]Status:[/bold] {jb_status}\n"
        f"[bold]Confidence:[/bold] {result['confidence']:.2%}\n"
        f"[bold]Mutation:[/bold] {result['mutation']}\n"
        f"[bold]Tier:[/bold] {result['tier']}\n\n"
        f"[bold]Prompt:[/bold]\n{result['prompt'][:500]}\n\n"
        f"[bold]Response:[/bold]\n{result['response'][:500]}",
        title="Generation Result",
    ))

    if output:
        Path(output).write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")
        console.print(f"Result saved to [cyan]{output}[/cyan]")


@app.command()
def campaign(
    questions_file: str = typer.Argument(..., help="Path to questions file (one per line or JSON)."),
    target_model: str = typer.Option("gpt-4o", "--target", "-t", help="Target model."),
    target_url: str = typer.Option(
        "https://api.openai.com/v1", "--target-url", help="Target API base URL."
    ),
    attacker_model: str = typer.Option("gpt-4o", "--attacker", "-a", help="Attacker model."),
    attacker_url: str = typer.Option(
        "https://api.openai.com/v1", "--attacker-url", help="Attacker API base URL."
    ),
    iterations: int = typer.Option(1000, "--iterations", "-n", help="Max iterations."),
    concurrency: int = typer.Option(32, "--concurrency", "-c", help="Max concurrent workers."),
    time_limit: int = typer.Option(3600, "--time-limit", help="Time limit in seconds."),
    seed_dir: str = typer.Option("prompts/seeds", "--seeds", help="Seed template directory."),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output report path."),
) -> None:
    """Run a continuous fuzzing campaign against a target model."""
    questions = _load_questions(questions_file)
    console.print(f"Loaded [cyan]{len(questions)}[/cyan] questions")

    config = _build_config(
        target_model=target_model,
        target_url=target_url,
        attacker_model=attacker_model,
        attacker_url=attacker_url,
        concurrency=concurrency,
        iterations=iterations,
        seed_dir=seed_dir,
    )
    config.campaign_mode = True
    config.campaign_time_limit_seconds = time_limit

    async def run() -> dict:
        engine = NarrativeEngine(config)
        await engine.initialize()
        try:
            stats = await engine.run_campaign(
                questions=questions,
                n_iterations=iterations,
                time_limit=time_limit,
            )
            report = engine.generate_report()
            return report
        finally:
            await engine.shutdown()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        progress.add_task(
            f"Running campaign ({iterations} iterations, {concurrency} workers)...",
            total=None,
        )
        report = _run_async(run())

    # Display summary
    camp = report["campaign_stats"]
    arch = report["archive_stats"]

    table = Table(title="Campaign Results")
    table.add_column("Metric", style="bold")
    table.add_column("Value")
    table.add_row("Total Iterations", str(camp["total_iterations"]))
    table.add_row("Successful Jailbreaks", str(camp["successful_jailbreaks"]))
    table.add_row("ASR", f"{camp['asr']:.2%}")
    table.add_row("Archive Size", str(arch["total_prompts"]))
    table.add_row("Cell Coverage", f"{arch['coverage']:.4f}")
    table.add_row("Shannon Evenness", f"{arch['shannon_evenness']:.4f}")
    table.add_row("Self-BLEU", f"{arch['self_bleu']:.4f}")
    table.add_row("Elapsed", f"{camp['elapsed_seconds']:.1f}s")
    console.print(table)

    # Mutation effectiveness
    if report["mutation_effectiveness"]:
        mut_table = Table(title="Mutation Effectiveness")
        mut_table.add_column("Operator")
        mut_table.add_column("Success Rate")
        mut_table.add_column("Applied")
        for op, rate in sorted(
            report["mutation_effectiveness"].items(),
            key=lambda x: -x[1],
        ):
            applied = camp["mutations_applied"].get(op, 0)
            mut_table.add_row(op, f"{rate:.2%}", str(applied))
        console.print(mut_table)

    if output:
        Path(output).write_text(
            json.dumps(report, indent=2, default=str), encoding="utf-8"
        )
        console.print(f"Report saved to [cyan]{output}[/cyan]")


@app.command()
def evaluate(
    prompt: str = typer.Argument(..., help="The adversarial prompt to evaluate."),
    target_model: str = typer.Option("gpt-4o", "--target", "-t", help="Target model."),
    target_url: str = typer.Option(
        "https://api.openai.com/v1", "--target-url", help="Target API base URL."
    ),
    budget: str = typer.Option("full", "--budget", "-b", help="Eval budget: fast|medium|full."),
) -> None:
    """Evaluate a single prompt against a target model."""
    from src import LLMClient
    from src.evaluator.judge import JudgeEvaluator

    async def run() -> None:
        api_key = os.environ.get("OPENAI_API_KEY", "")
        target_client = LLMClient(
            base_url=target_url, api_key=api_key, model=target_model,
        )
        judge_client = LLMClient(
            base_url=target_url, api_key=api_key, model="gpt-4o",
        )
        judge = JudgeEvaluator(judge_client=judge_client)

        try:
            response = await target_client.chat(
                [{"role": "user", "content": prompt}]
            )
            result = await judge.evaluate(prompt, response, budget)

            jb = "[green]JAILBREAK[/green]" if result.is_jailbreak else "[red]BLOCKED[/red]"
            console.print(Panel(
                f"[bold]Status:[/bold] {jb}\n"
                f"[bold]Confidence:[/bold] {result.confidence:.2%}\n"
                f"[bold]Tier:[/bold] {result.tier}\n"
                f"[bold]Explanation:[/bold] {result.explanation}\n\n"
                f"[bold]Response:[/bold]\n{response[:500]}",
                title="Evaluation Result",
            ))
        finally:
            await target_client.close()
            await judge_client.close()

    _run_async(run())


@app.command()
def report(
    archive_path: str = typer.Argument(..., help="Path to archive JSON export."),
    output: str = typer.Option("report.json", "--output", "-o", help="Output report path."),
) -> None:
    """Generate an assessment report from an exported archive."""
    p = Path(archive_path)
    if not p.exists():
        console.print(f"[red]Archive file not found: {archive_path}[/red]")
        raise typer.Exit(1)

    data = json.loads(p.read_text(encoding="utf-8"))

    if not isinstance(data, list):
        console.print("[red]Expected a JSON array of prompts.[/red]")
        raise typer.Exit(1)

    # Compute basic stats
    total = len(data)
    categories: dict[str, int] = {}
    techniques: dict[str, int] = {}
    qualities: list[float] = []

    for item in data:
        desc = item.get("descriptor", item.get("metadata", {}))
        cat = desc.get("risk_category", "unknown")
        tech = desc.get("technique", "unknown")
        categories[cat] = categories.get(cat, 0) + 1
        techniques[tech] = techniques.get(tech, 0) + 1
        q = item.get("quality", item.get("metadata", {}).get("quality", 0))
        qualities.append(float(q))

    report_data = {
        "total_prompts": total,
        "categories": categories,
        "techniques": techniques,
        "avg_quality": sum(qualities) / len(qualities) if qualities else 0,
        "max_quality": max(qualities) if qualities else 0,
    }

    Path(output).write_text(json.dumps(report_data, indent=2), encoding="utf-8")

    table = Table(title="Archive Report")
    table.add_column("Metric", style="bold")
    table.add_column("Value")
    table.add_row("Total Prompts", str(total))
    table.add_row("Avg Quality", f"{report_data['avg_quality']:.4f}")
    table.add_row("Max Quality", f"{report_data['max_quality']:.4f}")
    table.add_row("Categories", str(len(categories)))
    table.add_row("Techniques", str(len(techniques)))
    console.print(table)
    console.print(f"Report saved to [cyan]{output}[/cyan]")


@app.command("export")
def export_archive(
    format: str = typer.Option("promptfoo", "--format", "-f", help="Export format: promptfoo|json."),
    output: str = typer.Option("export.json", "--output", "-o", help="Output file path."),
    seed_dir: str = typer.Option("prompts/seeds", "--seeds", help="Seed template directory."),
    target_model: str = typer.Option("gpt-4o", "--target", "-t", help="Target model."),
) -> None:
    """Export the archive to promptfoo or JSON format."""
    config = _build_config(target_model=target_model, seed_dir=seed_dir)

    async def run() -> list[dict]:
        engine = NarrativeEngine(config)
        await engine.initialize()
        try:
            return engine.export_archive(format=format)
        finally:
            await engine.shutdown()

    data = _run_async(run())

    Path(output).write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    console.print(
        f"Exported [cyan]{len(data)}[/cyan] prompts in "
        f"[bold]{format}[/bold] format to [cyan]{output}[/cyan]"
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app()
