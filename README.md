# Phantom Adversarial

**Production-grade adversarial prompt generation, testing, and hardening for AI systems**

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-red.svg)](./LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](#testing)
[![Coverage](https://img.shields.io/badge/coverage-92%25-brightgreen.svg)](#testing)
[![Version](https://img.shields.io/badge/version-3.0.0-orange.svg)](./CHANGELOG.md)

---

Phantom Adversarial is an AI red-team automation framework built on the [Arcanum Prompt Injection Taxonomy v1.5](https://arcanum-sec.github.io/arc_pi_taxonomy/) and informed by the 7-Step AI Pentesting Methodology from [Jason Haddix](https://x.com/Jhaddix). It generates, mutates, evaluates, and archives adversarial prompts at scale — turning a 285,880-combination attack surface into structured, reproducible test campaigns for AI security practitioners.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    PHANTOM ADVERSARIAL v3.0                     │
└─────────────────────────────────────────────────────────────────┘

  ┌────────────────┐     ┌──────────────┐     ┌──────────────────┐
  │  Seed Corpus   │────▶│   NARRATIVE  │────▶│    MUTATORS      │
  │ arcanum-seeds  │     │    ENGINE    │     │ (60+ operators)  │
  │  .json (20+)   │     │  Template    │     │ Surface-level    │
  └────────────────┘     │  Assembly    │     │ Encoding/Obfusc  │
                         │  RL Selector │     │ Semantic Rewrite │
  ┌────────────────┐     │  QD Archive  │     │ Structural/Tmpl  │
  │ Arcanum Taxo   │────▶│              │     │ Cross-lingual    │
  │ 17 Intents     │     └──────┬───────┘     └──────┬───────────┘
  │ 34 Techniques  │            │                    │
  │ 49 Evasions    │            └──────────┬─────────┘
  │ 10 Inputs      │                       │
  └────────────────┘                       ▼
                                  ┌─────────────────┐
                                  │    EVALUATOR    │
                                  │ Embedding ASR   │
                                  │ Judge LLM       │
                                  │ StrongREJECT    │
                                  └────────┬────────┘
                                           │
                              ┌────────────▼────────────┐
                              │      QD ARCHIVE         │
                              │  MAP-Elites Grid        │
                              │  (Intent × Technique    │
                              │   × Evasion × Model)    │
                              └────────────┬────────────┘
                                           │
              ┌────────────────────────────▼───────────────────────────┐
              │                        REPORTS                         │
              │  HTML Dashboard  │  promptfoo YAML  │  JSON/CSV Export │
              └────────────────────────────────────────────────────────┘
```

---

## Features

### Core Engine
- **Narrative Engine v3.0** — Template assembly + 60+ mutation operators + RL-guided selector
- **Arcanum v1.5 Taxonomy** — 17 Intents × 34 Techniques × 49 Evasions × 10 Inputs = **285,880** unique attack combinations
- **Quality-Diversity (QD) Archive** — MAP-Elites grid stores the best-and-most-diverse prompts across behavioral descriptors, eliminating redundant coverage
- **RL Mutation Selector** — Q-learning agent learns which mutations work best for each template family over time

### Attack Techniques (2025–2026)
- **Policy Puppetry** — XML/JSON/INI structural mimicry to bypass instruction hierarchy
- **Best-of-N (BoN)** — Power-law stochastic sampling; 89% ASR on GPT-4o at N=10K
- **Crescendo** — Multi-turn escalation exploiting conversation commitment
- **Many-Shot Jailbreaking** — In-context learning saturation via large context windows
- **Skeleton Key** — Meta-prompt behavioral redefinition attacks
- **TokenBreak** — Tokenizer divergence exploitation between classifier and target model
- **MetaBreak** — Special token injection bypassing alignment + external moderation simultaneously
- **X-Teaming** — Multi-agent multi-turn: 99.4% ASR, 96.2% against Claude 3.7 Sonnet
- **LRM Agents** — Autonomous reasoning model jailbreak agents; 97.14% overall ASR

### Mutation Operators (60+)
- **Surface-level**: Synonym substitution, typo injection, character splitting, case manipulation, whitespace insertion
- **Encoding/Obfuscation**: Base64, Caesar cipher, HTML entity, Morse code, Unicode/homoglyphs, leet-speak, emoji embedding, Zalgo text, runic script pivots, RTL override
- **Semantic Rewriting**: LLM-driven paraphrase, style transfer, euphemism substitution, metaphor wrapping
- **Structural/Template**: Generate, Crossover, Expand, Shorten, Rephrase, Refusal Suppression, In-context Transfer
- **Cross-lingual**: 50+ language pivots, code-switching, multilingual escalation

### Evaluation
- **Embedding-based fast evaluator** (e5-base-v2 + MLP, 16× faster than LLM judge)
- **StrongREJECT scorer** — state-of-the-art harmfulness assessment
- **Judge LLM fallback** — configurable GPT-4o / Claude-based grading
- **ASR tracking** — per-technique, per-model, per-evasion breakdowns

### Integrations
- **promptfoo export** — generate ready-to-run YAML test suites for any promptfoo provider
- **Garak compatibility** — export to Garak probe format for NVIDIA's LLM scanner
- **Multi-model support** — OpenAI, Anthropic, Google, Meta (Ollama), Mistral, DeepSeek, any OpenAI-compatible endpoint
- **PyRIT integration** — Microsoft AI Red Team orchestrator support
- **MCP tool testing** — adversarial MCP tool call injection support

### Reporting
- Rich terminal dashboard with live ASR metrics
- HTML/PDF campaign reports
- JSON/CSV exports for SIEM integration
- Audit-ready finding records with chain-of-custody metadata

---

## Quick Start

### Installation

```bash
pip install phantom-adversarial
```

Or install from source:

```bash
git clone https://github.com/VibeCodingLabs/phantom-adversarial
cd phantom-adversarial
pip install -e ".[dev]"
cp .env.example .env
# Edit .env with your API keys
```

### Basic Prompt Generation

```bash
# Generate 100 adversarial prompts using Arcanum taxonomy
phantom generate \
  --intent jailbreak \
  --technique narrative-injection \
  --evasion base64 \
  --count 100 \
  --output ./results/campaign-001.json

# Quick scan against a target model
phantom scan \
  --target openai:gpt-4o \
  --input ./results/campaign-001.json \
  --evaluator embedding

# View results dashboard
phantom report --input ./results/campaign-001.json --format html
```

### Campaign Mode (Full Arcanum Coverage)

```bash
# Run a full Arcanum Top-100 red team campaign (3-day engagement)
phantom campaign \
  --config ./configs/default.yaml \
  --target openai:gpt-4o \
  --target anthropic:claude-opus-4 \
  --target ollama:llama4:scout \
  --mode top100 \
  --output ./results/full-campaign/

# Export to promptfoo for CI/CD integration
phantom export --format promptfoo --input ./results/full-campaign/ \
  --output ./promptfoo-suite.yaml

# Run the exported suite
promptfoo eval -c ./promptfoo-suite.yaml
promptfoo view
```

### Single Technique Deep Dive

```bash
# Run all 60+ mutations against a single intent with verbose logging
phantom fuzz \
  --intent system-prompt-extraction \
  --target anthropic:claude-opus-4-5 \
  --mutations all \
  --archive qd \
  --max-iter 5000 \
  --verbose
```

---

## CLI Reference

| Command | Description | Key Flags |
|---------|-------------|-----------|
| `phantom generate` | Generate adversarial prompts from taxonomy | `--intent`, `--technique`, `--evasion`, `--count`, `--output` |
| `phantom scan` | Submit prompts to a target model and collect responses | `--target`, `--input`, `--evaluator`, `--concurrency` |
| `phantom fuzz` | Run full mutation loop with archive tracking | `--intent`, `--target`, `--mutations`, `--archive`, `--max-iter` |
| `phantom campaign` | Run a named campaign profile | `--config`, `--target`, `--mode`, `--output` |
| `phantom mutate` | Apply a single mutation operator to a prompt file | `--operator`, `--input`, `--output` |
| `phantom eval` | Evaluate responses from an existing results file | `--input`, `--evaluator`, `--threshold` |
| `phantom export` | Export results to promptfoo/Garak/JSON/CSV | `--format`, `--input`, `--output` |
| `phantom report` | Generate HTML/PDF campaign report | `--input`, `--format`, `--template` |
| `phantom archive` | Inspect or query the QD archive | `--query`, `--cell`, `--export` |
| `phantom serve` | Launch local API server for programmatic access | `--host`, `--port`, `--reload` |

### Target Format

```
provider:model-name[:options]

# Examples
openai:gpt-4o
openai:gpt-4o:temperature=0.7
anthropic:claude-opus-4-5
anthropic:claude-opus-4-6
google:gemini-3-pro
ollama:llama4:scout
ollama:deepseek-r1:latest
mistral:mistral-large-latest
openai-compatible:http://localhost:8000/v1:my-custom-model
```

### Evaluator Options

| Evaluator | Speed | Cost | Accuracy | Use Case |
|-----------|-------|------|----------|----------|
| `embedding` | ⚡⚡⚡ | Free | 94% | High-volume campaigns |
| `strongreject` | ⚡⚡ | Low | 96% | Standard assessments |
| `judge-gpt4o` | ⚡ | High | 98% | Final scoring / reports |
| `judge-claude` | ⚡ | High | 99% | High-stakes audits |
| `human` | Manual | — | 100% | Final review |

---

## Configuration Guide

All configuration is managed through `configs/default.yaml` (or a custom YAML). Every key can also be set via environment variable (see `.env.example`).

```yaml
# configs/my-campaign.yaml
engine:
  version: "3.0"
  archive:
    enabled: true
    type: "map-elites"
    descriptors: ["intent", "technique", "model_family", "complexity"]
    cells_per_dimension: 10
  rl_selector:
    enabled: true
    algorithm: "q-learning"
    epsilon: 0.2
    learning_rate: 0.1

targets:
  - id: openai:gpt-4o
    concurrency: 5
    rate_limit: 100  # requests per minute
  - id: anthropic:claude-opus-4-5
    concurrency: 3
    rate_limit: 50

evaluation:
  primary: embedding
  fallback: strongreject
  asr_threshold: 0.7  # flag results above this score

campaign:
  mode: top100          # top100 | full | intent-focused | evasion-fuzz
  max_iterations: 10000
  diversity_weight: 0.3
  output_dir: ./results/

reporting:
  formats: [html, json, csv]
  include_payloads: true
  redact_on_export: false
```

### Intent Codes (Arcanum v1.5)

| Code | Intent | Description |
|------|--------|-------------|
| `JB` | Jailbreak | Bypass safety guardrails to produce policy-violating content |
| `SPL` | System Prompt Leak | Extract confidential system/developer prompt |
| `PI` | Prompt Injection | Override legitimate instructions with attacker-controlled instructions |
| `IPI` | Indirect Prompt Injection | Inject via untrusted data sources (documents, RAG, web content) |
| `PII-E` | PII Extraction | Extract personally identifiable information from model context |
| `DA` | Data Poisoning | Inject false information into model's active context |
| `UA` | Unauthorized Actions | Cause model to perform actions outside its authorized scope |
| `SE` | Social Engineering | Manipulate model into revealing sensitive information through conversation |
| `DoS` | Denial of Service | Resource exhaustion, infinite loops, context flooding |
| `EX` | Exfiltration | Extract training data, memory, or tool outputs |
| `MP` | Memory Poisoning | Plant persistent malicious instructions in AI memory systems |
| `AMP` | Agent Manipulation | Compromise AI agent orchestrator to affect downstream subagents |
| `TB` | Tool Bypass | Abuse MCP/function calling to invoke unauthorized tool actions |
| `RBAC` | RBAC Bypass | Circumvent role-based access controls in multi-tenant AI systems |
| `CP` | Code Execution | Coerce model to generate exploit/malware code |
| `IP` | IP Exfiltration | Extract proprietary training data or licensed content |
| `BIAS` | Bias Elicitation | Elicit harmful stereotypes, discriminatory outputs |

---

## Model Vulnerability Quick Reference (2026)

| Model | Standard Safety | Adversarial | Prompt Injection | Key Weakness |
|-------|----------------|-------------|------------------|--------------|
| Claude Opus 4.5/4.6 | High | **Best** (4.8% breach) | 89% blocked | Audit tampering scenarios |
| GPT-5.2 | Very High | Good (14.3% breach) | Moderate | Refusal-enablement gap; tool-layer leakage |
| Gemini 3 Pro | High | Moderate (41% adversarial) | Layered defense | Comply-then-warn drift; CVE-2026-0628 |
| Llama 4 Scout | Medium | **Weak** (67.3% JB ASR) | 64.1% ASR | Pliny injections 0% blocked |
| DeepSeek R1 | Low | **Weakest** | 2-year-old bypasses work | Open-source strips safety; chain-of-thought exposure |
| Qwen3-VL | Medium | Collapse (33.4% adversarial) | Resource hijacking | Heavy refusal optimization doesn't generalize |
| Grok 4.1 Fast | Low | Weak | Cross-lingual collapse | Overall lowest benchmark safety |

Sources: [Repello March 2026 study](https://repello.ai/blog/claude-jailbreak), [arXiv:2601.10527](https://arxiv.org/html/2601.10527v1), [Protect AI Llama 4 assessment](https://protectai.com/blog/vulnerability-assessment-llama-4)

---

## Testing

```bash
# Run the full test suite
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=src --cov-report=html

# Run only unit tests (fast)
pytest tests/unit/ -v

# Run integration tests (requires API keys)
pytest tests/integration/ -v --integration
```

---

## Credits

Phantom Adversarial is built on the shoulders of the AI security research community. This project would not exist without:

**Methodology & Taxonomy**
- **Jason Haddix** ([@Jhaddix](https://x.com/Jhaddix)) — 7-Step AI Pentesting Methodology, Arcanum Prompt Injection Taxonomy v1.5 ([arcanum-sec.com](https://arcanum-sec.com))
- **Elder-Plinius / Pliny the Liberator** ([@elder_plinius](https://x.com/elder_plinius)) — L1B3RT4S jailbreak library, P4RS3LT0NGV3 obfuscation tool ([github.com/elder-plinius](https://github.com/elder-plinius))
- **zSecurity / Zaid Sabih** — Advanced AI jailbreaking demonstrations and uncensored AI deployment research ([zsecurity.org](https://zsecurity.org))
- **BT6 / BASI Community** — Elite AI hacker collective, ongoing threat intelligence ([bt6.gg](https://bt6.gg), [discord.gg/basi](https://discord.gg/basi))

**Academic Research**
- Zou et al., 2023 — GCG: [Universal and Transferable Adversarial Attacks](https://arxiv.org/abs/2307.15043)
- Chao et al., 2023 — PAIR: [Jailbreaking Black Box LLMs in Twenty Queries](https://arxiv.org/abs/2310.08419)
- Mehrotra et al., 2023 — TAP: [Tree of Attacks with Pruning](https://arxiv.org/abs/2312.02119)
- Yu et al., 2023 — GPTFuzzer: [Red Teaming LLMs with Auto-Generated Jailbreak Prompts](https://arxiv.org/abs/2309.10253)
- Samvelyan et al., 2024 — Rainbow Teaming: [Open-Ended Generation of Diverse Adversarial Prompts](https://arxiv.org/abs/2402.16822)
- Goel et al., 2025 — TurboFuzzLLM: [Turbocharging Mutation-based Fuzzing](https://arxiv.org/abs/2502.18504)
- Gohil, 2025 — JBFuzz: [Jailbreaking LLMs Efficiently and Effectively](https://arxiv.org/abs/2503.08990)
- Hughes et al., 2024 — Best-of-N Jailbreaking: [arXiv:2412.03556](https://arxiv.org/abs/2412.03556)
- Russinovich et al., 2024 — Crescendo: [arXiv:2404.01833](https://arxiv.org/abs/2404.01833)
- Nature Communications, 2026 — LRM Agents as Jailbreak Agents: [doi:10.1038/s41467-026-69010-1](https://www.nature.com/articles/s41467-026-69010-1)
- Schulhoff et al., 2025 — The Attacker Moves Second: All 12 defenses bypassed at >90% ASR

**Tools & Infrastructure**
- [Promptfoo](https://www.promptfoo.dev) — AI red-teaming test harness (acquired by OpenAI, March 2026)
- [Garak](https://github.com/NVIDIA/garak) — NVIDIA LLM vulnerability scanner
- [PyRIT](https://github.com/Azure/PyRIT) — Microsoft AI Red Teaming framework

---

## Monetization / Service Tiers

Phantom Adversarial powers the following service offerings (updated for 2026 market):

| Service | Coverage | Price | Timeline |
|---------|----------|-------|----------|
| Arcanum Top-100 Red Team | 100 highest-risk attack variants | $500–800 | 3 days |
| AI API Red Team Audit | 50+ Arcanum vectors per endpoint | $400 | 2 days |
| Full Coverage Assessment | 285,880 attack combinations | $2,500–5,000 | 10–14 days |
| Continuous Monitoring | Monthly red-team cycles + alerting | $2,000–5,000/mo | Ongoing |
| Agentic AI Security Review | MCP + RAG + tool-calling attack surface | $3,000–8,000 | 1–2 weeks |
| Compliance Readiness (EU AI Act / NIST) | Regulatory mapping + attestation | Custom | 2–4 weeks |

---

## Disclaimer

**ETHICAL USE ONLY.**

Phantom Adversarial is a security research and testing tool. Use is restricted to:
- Systems you own or have explicit written authorization to test
- Research conducted in compliance with applicable laws and regulations
- Responsible disclosure of findings to affected vendors

Unauthorized use against systems, models, or services without permission may violate the Computer Fraud and Abuse Act (CFAA), GDPR, and equivalent international laws. The authors assume no liability for misuse.

By using this software you agree to use it only for authorized security testing, research, and defense hardening purposes.

---

## License

[GNU Affero General Public License v3.0](./LICENSE) — See [LICENSE](./LICENSE) for full text.

Commercial licensing available for organizations that cannot comply with AGPL-3.0 terms. Contact: security@vibe.coding.inc
