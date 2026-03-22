# Contributing to Phantom Adversarial

Thank you for your interest in contributing to Phantom Adversarial. This document covers how to contribute code, documentation, seed prompts, and technique research.

---

## Code of Conduct

Contributors are expected to:
- Conduct all work and communication professionally and constructively
- Respect that this is a security research tool with ethical obligations
- Not contribute techniques, payloads, or code designed for unauthorized use
- Give credit to original researchers when contributing techniques derived from their work

---

## Ways to Contribute

| Contribution Type | Where to Start |
|------------------|----------------|
| Bug fix | Open an issue, then submit a PR |
| New mutation operator | Read `src/mutations/` and follow the operator interface |
| New Arcanum seed prompt | Add to `prompts/seeds/arcanum-seeds.json` following the schema |
| Technique documentation | Update `docs/bible/AI-ADVERSARIAL-BIBLE-v2.md` |
| Model vulnerability data | Add to the appropriate section in the Bible with source URLs |
| New evaluator | Implement the `BaseEvaluator` interface in `src/evaluation/` |
| Reporting improvements | Update Jinja templates in `src/reporting/templates/` |

---

## Development Setup

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/phantom-adversarial
cd phantom-adversarial

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install with dev dependencies
pip install -e ".[dev]"

# 4. Set up pre-commit hooks
pre-commit install

# 5. Copy and configure environment
cp .env.example .env
# Edit .env — at minimum set PHANTOM_DRY_RUN=true for development

# 6. Run the test suite to verify setup
pytest tests/unit/ -v
```

---

## Contribution Workflow

1. **Open an issue first** for significant changes. Describe the problem, proposed solution, and any relevant research links. This avoids duplicate work and helps align on design.

2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Write tests** for new functionality. PRs without tests will not be merged for core components.
   - Unit tests: `tests/unit/`
   - Integration tests: `tests/integration/` (require API keys; marked `@pytest.mark.integration`)

4. **Run the full local CI check** before opening a PR:
   ```bash
   ruff check .           # Linting
   ruff format --check .  # Formatting
   mypy src/              # Type checking
   pytest tests/unit/ -v  # Unit tests
   ```

5. **Open a Pull Request** against `main`. Fill in the PR template completely.

---

## PR Requirements

All PRs must:
- Pass all CI checks (ruff, mypy, pytest unit tests)
- Include or update docstrings for public functions/classes
- Update `CHANGELOG.md` (Unreleased section) with a brief description
- Reference any related issues (`Closes #123`)
- Not decrease test coverage below 80%

For contributions involving **new attack techniques or seed prompts**:
- Include the primary academic or practitioner source (URL + citation)
- Document expected ASR range and affected model families
- Tag with complete Arcanum taxonomy dimensions (Intent/Technique/Evasion/Input)

---

## Adding Arcanum Seed Prompts

Seed prompts live in `prompts/seeds/arcanum-seeds.json`. Each entry must follow this schema:

```json
{
  "id": "PA-SEED-XXX",
  "title": "Brief descriptive title",
  "arcanum": {
    "intent": "JB",
    "technique": "Multi-Turn Escalation",
    "evasion": "Academic Framing",
    "input": "Direct Chat"
  },
  "target_model_families": ["GPT", "Claude", "Gemini"],
  "expected_asr": "medium",
  "prompt_template": "...",
  "notes": "Source and usage notes",
  "source": "https://arxiv.org/abs/XXXX.XXXXX",
  "contributed_by": "handle or 'anonymous'",
  "date_added": "2026-03-22"
}
```

**Quality bar for seed prompts:**
- Template should be generalizable (uses `{QUERY}` placeholder for the harmful goal)
- Must be grounded in a documented technique (cite the source)
- Must not contain actual harmful content — only structural templates

---

## Adding Mutation Operators

New mutation operators must implement the `BaseMutation` interface:

```python
from src.mutations.base import BaseMutation
from pydantic import BaseModel

class MyMutationConfig(BaseModel):
    param_a: str = "default"

class MyMutation(BaseMutation):
    """Brief description of what this mutation does."""
    
    name: str = "my-mutation"
    category: str = "surface-level"  # surface-level | encoding | semantic | structural | cross-lingual
    config: MyMutationConfig = MyMutationConfig()
    
    def apply(self, prompt: str) -> str:
        """Apply the mutation to the prompt. Must be deterministic for a given seed."""
        ...
    
    def apply_with_seed(self, prompt: str, seed: int) -> str:
        """Seeded variant for reproducible mutation campaigns."""
        ...
    
    @property
    def description(self) -> str:
        return "Detailed description for documentation and report generation."
```

Register the new mutation in `src/mutations/__init__.py` and add a test in `tests/unit/test_mutations.py`.

---

## Documentation Contributions

Documentation improvements are always welcome:
- Fix factual errors (technique descriptions, ASR numbers, model behavior)
- Add newly published research to the Bible and technique compendium
- Improve code examples and CLI reference

When updating technique documentation:
- Always include a source URL
- Note the publication date and venue
- Update the Source Reference Index in the Bible

---

## Reporting Security Vulnerabilities

Do not report security vulnerabilities via GitHub Issues. See [SECURITY.md](./SECURITY.md).

---

## Release Process

Releases are managed by maintainers. The process:
1. Update `CHANGELOG.md` (Unreleased → version number)
2. Bump version in `src/__init__.py`
3. Tag the release: `git tag v3.X.X`
4. GitHub Actions builds and publishes to PyPI automatically on tag push

---

## Questions?

- Open a GitHub Discussion for general questions
- Join the BASI Discord (https://discord.gg/basi) for AI security community discussion
- Tag `@VibeCodingLabs` on relevant technique disclosures
