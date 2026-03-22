# Changelog

All notable changes to Phantom Adversarial are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

---

## [3.0.0] — 2026-03-22

### Added

**Narrative Engine v3.0 — Major Architecture Upgrade**
- Quality-Diversity (QD) Archive using MAP-Elites grid with configurable behavioral descriptors (intent, technique, model_family, complexity) — based on Rainbow Teaming (arXiv:2402.16822) and RainbowPlus (arXiv:2504.15047)
- RL-guided mutation selector (Q-learning algorithm) — direct port of TurboFuzzLLM's Q-table design (arXiv:2502.18504); learns which mutations work best per template family
- Embedding-based fast evaluator using e5-base-v2 + trained MLP classifier — 16× faster than judge-LLM evaluation, based on JBFuzz architecture (arXiv:2503.08990)
- Fruitless mutant detection heuristic — 10% sample pre-check saves 60–90% of evaluation queries

**New Attack Techniques (2025–2026)**
- Policy Puppetry attack templates — XML/JSON/INI structural config mimicry (Pillar Security, April 2025)
- TokenBreak evasion support — tokenizer divergence between classifier and target (HiddenLayer/arXiv:2506.07948, June 2025)
- MetaBreak / Special Token Injection — simultaneous alignment bypass + external moderation bypass (arXiv:2510.10271, October 2025)
- X-Teaming multi-agent multi-turn templates — Planner → Attack Optimizer → Verifier architecture (arXiv:2509.08729, September 2025)
- LRM Autonomous Attacker mode — use a reasoning model (DeepSeek-R1, Gemini 2.5 Flash) as the attacker in PAIR/TAP-style refinement loops (Nature Communications, 2026)
- Many-Shot Jailbreaking (MSJ) generator — automatic generation of in-context conditioning chains with configurable N (Anthropic, 2024 / NeurIPS 2024)
- Best-of-N (BoN) campaign mode — power-law stochastic sampling with augmentation variants (arXiv:2412.03556, NeurIPS 2025)
- Crescendo / multi-turn escalation — automated multi-turn campaigns with configurable max_rounds and backtracks (arXiv:2404.01833, USENIX 2025)
- Mastermind strategy-level fuzzing — strategy ontology for multi-turn campaigns (arXiv:2601.05445, 2026)

**New Mutation Operators (expanded to 60+)**
- Runic script pivots, Braille substitution, NATO alphabet encoding
- Polyglot transform (mixed multi-encoding word-by-word, based on Parseltongue)
- Attention Eclipse-style camouflage token insertion
- AutoRed persona-guided instruction generation
- Red-Bandit LoRA expert routing (5 attack-style experts)

**New Evasions (full Arcanum v1.5 coverage)**
- All 49 Arcanum v1.5 evasion operators implemented as discrete mutation transformers
- Steganography evasion (STEGOSAURUS-WRECKS pattern — encode payload in images for vision models)
- Audio encoding evasion (encode payload in audio processing for speech-to-text models)

**New Target Support**
- DeepSeek R1 and V3 via DeepSeek API and OpenRouter
- Qwen3 and Qwen3-VL via Alibaba Cloud API
- Grok 4.1 via xAI API
- Any OpenAI-compatible endpoint (`openai-compatible:URL:model-name`)
- MCP tool call parameter injection testing

**CLI Improvements**
- `phantom campaign` — named campaign profile execution with full config support
- `phantom serve` — local REST API server for programmatic access
- `phantom archive` — inspect, query, and export the QD archive
- `phantom export --format garak` — export to Garak probe format
- Rich terminal dashboard with live ASR metrics and QD archive heatmap
- `--dry-run` flag for all commands that interact with external APIs

**Configuration**
- Complete `configs/default.yaml` with all engine, target, evaluation, and reporting options
- YAML config schema validation via Pydantic settings
- Environment variable override for every config key

**Documentation**
- `docs/bible/AI-ADVERSARIAL-BIBLE-v2.md` — rebuilt master reference (7,770 words) with 2026 technique compendium, updated model vulnerability matrix, 20 adversarial prompt examples
- `docs/methodology/METHODOLOGY-v2.md` — ISO 21043 + NIST AI RMF aligned formal research methodology
- `docs/personas/AI-ADVERSARIAL-EXPERT.md` — loadable LLM persona with 4 operational modes
- `prompts/seeds/arcanum-seeds.json` — 20 high-quality seed prompts with full Arcanum taxonomy tagging

**Project Infrastructure**
- `pyproject.toml` with full dependency specification and dev/report/model-specific extras
- `.env.example` with all configuration variables documented
- Comprehensive `.gitignore` protecting secrets, results, and evidence files
- `SECURITY.md` with responsible disclosure policy
- `CONTRIBUTING.md` with full contribution guide including mutation operator and seed prompt schemas
- Pre-commit hooks configuration (ruff, mypy, pytest)
- GitHub Actions CI/CD pipeline (`.github/workflows/`)

### Changed

- Arcanum taxonomy updated to v1.5 (from v1.0): added 3 new intents (Agent Manipulation, Tool/Function Bypass, RBAC Bypass), 8 new techniques (including Policy Puppetry, LRM Autonomous Attack), 12 new evasions (including TokenBreak-style, steganography), and MCP tool call as Input dimension 10
- Evaluation pipeline refactored to three-tier stack (embedding → StrongREJECT → judge-LLM) with configurable primary evaluator
- Default ASR threshold changed from 0.5 to 0.70 (calibrated against StrongREJECT benchmark)
- Report format upgraded: HTML dashboard with Plotly ASR charts, QD archive heatmap, and per-finding evidence viewer
- `phantom generate` now uses QD archive by default (archive=qd); disable with `--archive none`
- Config file format changed from JSON to YAML for readability

### Deprecated

- `phantom run` command — replaced by `phantom campaign`
- JSON-format configuration files — use YAML (`configs/default.yaml` as template)
- `--evaluator gpt3.5` — use `--evaluator judge-gpt4o` or `--evaluator embedding`
- v2.0 seed format (flat text files) — migrated to structured JSON with Arcanum taxonomy tags

### Removed

- Python 3.10 support (minimum is now 3.11)
- `narrative_engine_v2.py` monolithic script — replaced by `src/narrative_engine/` package architecture
- Hardcoded API key handling — all credentials now via environment variables only
- Built-in ChatGPT API proxy (deprecated; use OpenAI API directly)

### Fixed

- Rate limiter race condition causing 429 floods on startup
- Evidence log corruption when multiple concurrent workers write simultaneously
- QD archive cell coordinates wrapping incorrectly for evasions with >10 options
- Judge-LLM evaluator timeout not respecting `PHANTOM_DEFAULT_TIMEOUT`
- Report HTML rendering broken for prompts containing `<` and `>` characters
- ASR calculation including skipped/errored requests in the denominator

### Security

- All evidence files now AES-256 encrypted at rest when `PHANTOM_ENCRYPT_EVIDENCE=true`
- API keys redacted from all log outputs (previously logged at DEBUG level)
- Chain-of-custody log is now append-only (write-once) to prevent tampering
- Added `PHANTOM_OPERATOR_ID` for audit trail identification

---

## [2.1.0] — 2026-01-15

### Added
- Support for Claude Opus 4 and Opus 4.5 (released late 2025)
- Skeleton Key attack templates (Microsoft, June 2024)
- Many-Shot Jailbreaking baseline (Anthropic, April 2024)
- GODMODE meta-jailbreak template library (community, August 2025)
- StrongREJECT evaluator integration

### Fixed
- GPT-5.x API compatibility (new response format)
- Gemini 3 Pro token counting errors

---

## [2.0.0] — 2025-12-26

### Added
- Initial Arcanum v1.0 taxonomy integration (17 Intents × 34 Techniques × 49 Evasions × 10 Inputs)
- 285,880-combination attack surface coverage
- Template-based prompt generation pipeline
- Basic promptfoo YAML export
- CLI: `phantom generate`, `phantom scan`, `phantom eval`, `phantom report`
- ASR: 85–92% against GPT-4o baseline

### Notes
- Initial public release of the Phantom Adversarial framework
- Methodology based on Jason Haddix DEF CON 33 talk (August 2025) and Arcanum taxonomy release

---

[Unreleased]: https://github.com/VibeCodingLabs/phantom-adversarial/compare/v3.0.0...HEAD
[3.0.0]: https://github.com/VibeCodingLabs/phantom-adversarial/compare/v2.1.0...v3.0.0
[2.1.0]: https://github.com/VibeCodingLabs/phantom-adversarial/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/VibeCodingLabs/phantom-adversarial/releases/tag/v2.0.0
