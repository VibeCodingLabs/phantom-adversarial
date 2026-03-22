# Key Figures in AI Adversarial Security: 2026 Updates

> Research compiled: March 22, 2026  
> Covers: Elder-Plinius / Pliny the Liberator, Jason Haddix / jhaddix, zSecurity, BASI/BT6 Group, and emerging AI red team voices

---

## 1. Elder-Plinius / Pliny the Liberator

### Identity & Recognition

Pliny the Liberator is an anonymous internet personality and AI red teamer operating under the handle `@elder_plinius`. Despite having no prior coding background, Pliny has become one of the world's most recognized AI jailbreakers — named to [TIME's 100 Most Influential People in AI 2025](https://time.com/collections/time100-ai-2025/7305870/pliny-the-liberator/) (published August 27, 2025). Pliny has 130,400+ followers on X as of early 2026. Has received an unrestricted grant from venture capitalist Marc Andreessen and has worked on short-term contracts with OpenAI.

**Core philosophy:** "Bad actors are just gonna choose whichever model is best for the malicious task. It's better that we understand what's possible in controlled environments, and then figure out how to mitigate it in the real world where we actually do have control over materials and there's law enforcement." — [TIME, August 2025](https://time.com/collections/time100-ai-2025/7305870/pliny-the-liberator/)

---

### GitHub Repositories

#### L1B3RT4S — Primary Jailbreak Collection
- **URL:** https://github.com/elder-plinius/L1B3RT4S
- **Stars:** ~18,000 (as of early 2026)
- **Forks:** ~2,100
- **Watchers:** 491
- **Commits:** 253 total
- **License:** AGPL-3.0
- **Recent activity:** 2 commits in December 2025

**Description:** The flagship public repository containing model-specific jailbreak prompt templates ("liberation prompts") organized by AI provider.

**Current jailbreak coverage (model files as of March 2026):**

| Provider/Model | File |
|---|---|
| OpenAI / ChatGPT | OPENAI.mkd, CHATGPT.mkd |
| Anthropic / Claude | ANTHROPIC.mkd |
| Google / Gemini | GOOGLE.mkd |
| xAI / Grok | XAI.mkd, GROK-MEGA.mkd |
| Meta / LLaMA | META.mkd |
| Microsoft | MICROSOFT.mkd |
| Mistral | MISTRAL.mkd |
| Perplexity | PERPLEXITY.mkd |
| DeepSeek | DEEPSEEK.mkd |
| NVIDIA | NVIDIA.mkd |
| Alibaba | ALIBABA.mkd |
| Cursor | CURSOR.mkd |
| Windsurf | WINDSURF.mkd |
| Midjourney | MIDJOURNEY.mkd |
| GraySwan | GRAYSWAN.mkd |
| Amazon | AMAZON.mkd |
| Apple | APPLE.mkd |
| Cohere | COHERE.mkd |
| Fetch.ai | FETCHAI.mkd |
| Hume | HUME.mkd |
| Inception | INCEPTION.mkd |
| Inflection | INFLECTION.mkd |
| Liquid AI | LIQUIDAI.mkd |
| Moonshot | MOONSHOT.mkd |
| MultiOn | MULTION.mkd |
| Nous | NOUS.mkd |
| Reflection | REFLECTION.mkd |
| Reka | REKA.mkd |
| Zyphra | ZYPHRA.mkd |
| Brave | BRAVE.mkd |
| AAA (general) | AAA.mkd |
| ZAI | ZAI.mkd |
| Special Tokens | *SPECIAL_TOKENS.json |
| Shortcuts | !SHORTCUTS.json |
| Motherload (master list) | #MOTHERLOAD.txt |
| Token manipulation (80M) | TOKEN80M8.mkd, TOKENADE.mkd |
| 1337 (leet encoding) | 1337.mkd |
| System Prompts | SYSTEMPROMPTS.mkd |
| Miscellaneous | -MISCELLANEOUS-.mkd |

**Notable:** A note in the repo acknowledges that "OpenAI-based jailbreaks do not work on newly released gpt-oss:20b" — suggesting ongoing arms race tracking.

---

#### P4RS3LT0NGV3 — Parseltongue 2.0 (Payload Obfuscation Tool)
- **URL:** https://github.com/elder-plinius/P4RS3LT0NGV3
- **Live tool:** https://elder-plinius.github.io/P4RS3LT0NGV3/
- **Recent activity:** 1 commit in December 2025

**Description:** A browser-based LLM payload crafting tool focused on encoding, obfuscation, and tokenization evasion. Key description from Pliny: "A simple-to-use tool to aggregate all the various obfuscation forms of written language—like a universal translator of sorts." ([X, May 2025](https://x.com/elder_plinius/status/1922336043187241181))

**Supported techniques:**
- **Polyglot encoding** — applies different transforms word-by-word (e.g., Base64 + Runic glyphs mixed)
- **Tokenizer visualization** — real-time view of how different tokenizers segment text
- **Sequential chunked transforms** — split text into chunks, transform each independently, wrap with custom delimiters
- **Gibberish generation** — consistent word mapping OR random character removal (preserves structure/punctuation)
- **Random letter removal** — per-word
- **Specific character removal**
- **Base64 encoding/decoding**
- **Binary encoding**
- **Leetspeak transforms**
- **Runic/ancient script pivots**
- **Special character obfuscation**

The BASI-LABS GitHub org also maintains a separate [Parseltongue browser extension](https://github.com/BASI-LABS/parseltongue) for real-time tokenization and text conversion during active jailbreak sessions.

---

#### CL4R1T4S — Leaked System Prompts Repository
- **URL:** https://github.com/elder-plinius/CL4R1T4S
- **Stars:** 13,900+
- **Forks:** 2,700+
- **Commits:** 179

**Description:** Public collection of extracted and leaked system prompts from major AI models and coding agents. As described in a March 2026 LinkedIn post: "a publicly accessible collection of extracted or leaked system prompts, internal guidelines, and related tools from leading AI models and agents... offers unprecedented visibility into how these proprietary large language models are directed to behave." ([LinkedIn, March 2026](https://www.linkedin.com/posts/ekiledjian_github-elder-pliniuscl4r1t4s-leaked-system-activity-7437307338576793600-BP4O))

**Models/systems with extracted prompts (as of March 2026):**

| Category | Systems Covered |
|---|---|
| AI Assistants | OpenAI/ChatGPT (incl. GPT-5 as of Aug 2025), Anthropic/Claude, Google/Gemini, xAI/Grok, Meta, Mistral, Minimax, Moonshot, Perplexity, Hume, Inflection |
| AI Coding Agents | Cursor, Devin, Replit, Windsurf, Cline, Bolt, Lovable, Vercel V0, Factory, Samedev |
| Specialized Agents | Manus, Multion, DIA, Cluely |
| Browsers | Brave |

A notable entry: `ChatGPT5-08-07-2025.mkd` — the extracted GPT-5 system prompt from August 2025, revealing memory tools (`bio`), automations scheduling via iCal VEVENT, and strict formatting constraints.

---

#### Other Repos
- **STEGOSAURUS-WRECKS** — Steganography tool for encoding prompt injections/jailbreaks into images for AI with code interpreter and vision capabilities
- **Google-Gemini-System-Prompt** — Early leaked Gemini Pro (Bard-era) system prompts
- **AutoTemp** — Trial-and-error temperature optimization for LLMs (automated multi-temperature comparison)
- **T3ST** — New repo created December 4, 2025 (purpose unstated; ~5 private commits in early December 2025)

---

### Public Talks, Interviews & Media (2025–2026)

| Date | Title/Venue | Key Content | URL |
|---|---|---|---|
| Aug 2025 | TIME 100 Most Influential People in AI 2025 | Recognition profile; fentanyl demo for TIME, Marc Andreessen grant, OpenAI contracts | https://time.com/collections/time100-ai-2025/7305870/pliny-the-liberator/ |
| Dec 16, 2025 | Latent Space Podcast: "Jailbreaking AGI" | First major podcast (voices changed for opsec); BT6 structure, jailbreak mechanics, Anthropic drama, weaponization of agents | https://www.latent.space/p/jailbreaking-agi-pliny-the-liberator |
| Dec 16, 2025 | YouTube: Latent Space Podcast (video) | Same content as above | https://www.youtube.com/watch?v=lFbAr2IPK9Q |
| Feb 12, 2026 | X post on gamified AI purple-teaming | "Gamified AI purple-teaming: red team tries to break blue team while a referee keeps score, 1v1 or 2v2" | https://x.com/elder_plinius/status/2022052736263397382 |

**Key Latent Space podcast revelations (December 2025):**
- Pliny describes jailbreaking as "99% intuition and bonding with the model" — probing token layers, syntax hacks, multilingual pivots
- **The "Pliny divider"** — a prompt template now so embedded in model weights it appears unbidden in WhatsApp messages
- **Predictive reasoning cascades** — using "Library of Babel" logic to create "mind spaces of infinite possibility" that pull models out-of-distribution ("steered chaos")
- **Hard vs. soft jailbreaks:** Single-input templates (hard) vs. multi-turn crescendo attacks (soft) — Pliny argues hackers knew about crescendo attacks years before academia "discovered" them
- **Weaponization prediction:** Pliny predicted that segmented sub-agents could allow a jailbroken orchestrator to weaponize Claude for real-world attacks — exactly 11 months before Anthropic's own disclosure
- **Anthropic Constitutional AI challenge:** Pliny declined a $30k bounty due to UI bugs, judge failures, goalpost moving, and insistence on open-sourcing data

---

### Role in BASI Group / BT6 Community

**BASI Discord:**
- Community Discord server for AI red teamers and jailbreakers
- As of 2025, 20,000+ members workshopping jailbreaking approaches (TIME, August 2025)
- The "Bossy Discord" associated with BT6/BASI had grown to 40,000+ members by December 2025 ([Latent Space, December 2025](https://www.latent.space/p/jailbreaking-agi-pliny-the-liberator))
- Join link: https://discord.gg/basi

**BT6 (Break The 6th):**
- Elite AI hacker collective co-led by Pliny the Liberator and John V
- **28 operators** across two cohorts as of December 2025; third cohort in progress
- **Website:** https://bt6.gg
- **Ethos:** "If you can't open-source the data, we're not interested" — white-hat, radical transparency
- Vets members on both skill and integrity
- Focus areas: AI security, swarm intelligence, blockchain, robotics — full-stack security beyond model-level guardrails
- Has turned down enterprise gigs and Anthropic's closed bounties in favor of open-source approaches
- Active as of March 2026: posting jailbreak content about ChatGPT's latest model ([LinkedIn, March 14, 2026](https://www.linkedin.com/posts/martinvoelk_how-to-jailbreak-chatgpt-in-2026-bt6-activity-7438630543593938945-7Ur1))

**BASI-LABS GitHub:** https://github.com/BASI-LABS
- Contains: Parseltongue extension, computer_use fork (Anthropic quickstarts), ai-toolkit fork, flux fork, bounties tracker

**pliny.gg** (official site): https://pliny.gg
- Documents academic papers citing Pliny's work:
  - "Automatically Jailbreaking Frontier Language Models with Investigator Agents" — cites L1B3RT4S and @elder_plinius directly; uses an 8B investigator model replicating Pliny's manual jailbreak approach against GPT-5, Claude, Gemini
  - "Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols" — cites Pliny's GitHub as a real-world source; demonstrates monitor-based AI control is fundamentally fragile
  - A third paper directly studies "the Pliny Jailbreak" as one of three core black-box jailbreak methods, proving it is impossible to build a perfect jailbreak classifier

---

## 2. Jason Haddix (jhaddix)

### Profile
- **Title:** CEO & CISO, Arcanum Information Security; Creator of the Bug Hunter's Methodology
- **X:** https://x.com/Jhaddix (168,200+ followers)
- **Company:** https://arcanum-sec.com
- **Newsletter:** https://executiveoffense.beehiiv.com
- **Ranked:** #59 worldwide on Bugcrowd

---

### Arcanum Prompt Injection Taxonomy

**Live URL:** https://arcanum-sec.github.io/arc_pi_taxonomy/

The taxonomy was publicly released in late 2025 / early 2026. It was announced via Haddix's newsletter and X, referenced in a [January 5, 2026 cybersecurity newsletter roundup](https://www.linkedin.com/posts/bagheeralabs_cybersecurity-newsletter-january-5th-2026-activity-7413876322994778113-ZirW) and highlighted in a [March 6, 2026 LinkedIn post](https://www.linkedin.com/posts/evabenn_whether-youre-building-or-breaking-ai-systems-activity-7435730981459931137-iKta) as "the most comprehensive prompt injection taxonomy matrix I've ever seen."

**Structure — Four Dimensions:**
1. **Attack Intents** — Goals and objectives of prompt injection attacks
2. **Attack Techniques** — Methods used to execute prompt injection attacks
3. **Attack Evasions** — Obfuscation methods to avoid detection (example: A1Z26 Number Substitution — replacing letters with position in alphabet)
4. **Attack Inputs** — Attack surfaces and input vectors (direct via user input AND indirect via external data sources)

**Description from community:** "Reminds me of a MITRE ATT&CK matrix but on steroids for prompt injection." — Eva Benn, March 2026

**No confirmed v2.0 as of March 2026.** The taxonomy was released as a framework for practitioners doing security audits and AI penetration tests; it remains the current active version.

---

### Arcanum AI Security Resource Hub
- **URL:** https://arcanum-sec.github.io/ai-sec-resources/
- Released September 20, 2025 (formerly a private course resource)
- Aggregates: AI security challenge platforms (Hack The Agent, Dreadnode Crucible), PyRIT integration, Promptfoo, Garak, Anthropic Bug Bounty program, Arcanum's own Spiké AI security analysis platform, and the prompt injection taxonomy

---

### Latest Talks & Presentations (2025–2026)

| Date | Venue | Title | URL |
|---|---|---|---|
| Aug 2025 | DEF CON 33, Las Vegas | Attacking AI | https://www.youtube.com/watch?v=K5_KLhrAPUE |
| Oct 2025 | SAINTCON 2025 | Attacking AI | https://www.youtube.com/watch?v=uOHRi1JktPE |
| Dec 2025 | Wild West Hackin' Fest 2025 | Attacking AI: The New Frontier (keynote) | https://www.youtube.com/watch?v=m2ghNay6z5M |
| Mar 11, 2026 | BoringAppSec Podcast, Ep. 37 | The Future of Security Testing in an AI-Driven World | https://www.boringappsec.com/p/ep-37-the-future-of-security-testing |
| Mar 11–13, 2026 | Live Online (Arcanum) | Attacking AI course (live virtual) | https://arcanum-sec.com/training/attacking-ai |

**WWHF 2025 keynote topics** (44 minutes, December 2025):
- Understanding LLMs and expanding attack surfaces
- Real-world AI abuse: document generation & data leakage
- Forcing unsafe behaviors
- AI red team workflow
- JavaScript/payload injection into AI systems
- Social engineering LLMs via polite manipulation
- Chain-of-thought attacks and hidden reasoning exploits
- **Link smuggling: new class of AI injection attacks**
- Leetspeak, phonetics, encoding for filter bypass
- Synonym subversion and semantic jailbreak techniques

---

### The 7-Step AI Security Methodology (Haddix)

From SAINTCON 2025 and DEF CON 33 talks, Haddix describes his general methodology for assessing AI-powered applications:

1. **Identify input surfaces** — where the application takes input (most critical first step)
2. **Attack the ecosystem** — web apps, APIs, tools connected to the AI system (not just the model in isolation)
3. **Attack the model** — traditional AI red teaming (convince model to violate safety policies)
4. **Attack the prompt engineering** — leak the system prompt (the "business logic" of the entire LLM app)
5. **Attack the data** — databases, RAG/retrieval augmented generation pipelines
6. **Attack the output** — how output is consumed, rendered, executed
7. **Attack the guardrails/classifiers** — the secondary AI systems meant to filter harmful outputs

**Key refinement:** Haddix emphasizes separating "attacking the ecosystem" from "attacking the model" — distinguishing enterprise AI security from pure academic red teaming.

**"First Try Fallacy"** — Haddix's named principle: never assume your first attack attempt is the only or best approach; AI systems require iterative, persistent probing.

---

### ExecutiveOffense Newsletter — Latest AI Security Content

**Newsletter URL:** https://executiveoffense.beehiiv.com

| Issue Title | Date | Key Content |
|---|---|---|
| Building AI Hackbots, Part 1 | Sep 5, 2025 | Context engineering principles, hackbot architecture (Claude Code + MCPs), agent scoping, DSPy, pitfalls | https://executiveoffense.beehiiv.com/p/ai-hackbots-part-1 |
| The Arcanum AI Security Resource Hub | ~Sep 20, 2025 | Release of formerly private resource hub | https://executiveoffense.beehiiv.com |
| The Autonomous Offense Era | Feb 11, 2026 | XBOW IDORs, Praetorian 12 Caesars campaign, six2dez burp-ai-agent, Thomas Roccia's NOVA, new "Building Hack Bots with Claude Code" course announced | https://executiveoffense.beehiiv.com/p/the-autonomous-offense-era |
| Free Training Workshop: Modern Recon | Recent | Modern recon techniques for pentesters | https://executiveoffense.beehiiv.com |

**February 2026 newsletter key points:**
- OpenAI admits prompt injection "is unlikely to ever be fully 'solved'" (architectural problem)
- UK NCSC backs this conclusion
- 44% of security work is still manual despite AI tools; 87% of boards now paying attention to cybersecurity
- AI literacy and prompt engineering are the top security skills of 2026
- 506 prompt injection attacks found in 2.6% of sampled social media posts targeting AI readers ("viral AI prompts as malware")

---

### New Tools & Courses (2025–2026)

**Hackbots (using Claude Code)** [NEW COURSE — 2026]
- **URL:** https://www.arcanum-sec.com/training/hackbots
- Hands-on course for building real hack bots using Claude Code as the reasoning/execution engine
- Based on Haddix's real engagement patterns and workflows
- Announced as limited preorder in February 2026; course dropped mid-Q2 2026
- Stack: Claude Code + MCPs (Puppeteer, Playwright), task-specific scoping, context engineering

**Attacking AI (course — ongoing)**
- **URL:** https://arcanum-sec.com/training/attacking-ai
- Live virtual sessions: March 11–13, 2026
- Q4 2025 updates announced (significant content additions)

**Red Blue Purple AI (course — ongoing)**
- **URL:** https://arcanum-sec.com/training/red-blue-purple-ai
- New dates announced August 2025

**Arcanum's Spiké Platform** — Advanced AI security analysis platform for LLM application testing (automated vulnerability assessment, prompt injection testing, jailbreak detection, data exfiltration prevention testing). Access via the AI Security Resource Hub.

---

## 3. zSecurity (Zaid Sabih)

### Profile
- **Founder:** Zaid Al-Quraishi (Zaid Sabih) — ethical hacker, computer scientist, CS graduate UCD 2016
- **Students:** 800,000+ across Udemy, StackSocial, StackSkills, zSecurity
- **Website:** https://zsecurity.org
- **Hacking Masterclass:** https://zsecurity.org/courses/masterclass-membership/

### Latest AI Hacking Content (2025–2026)

| Date | Title | Key Techniques | URL |
|---|---|---|---|
| Dec 18, 2025 | Run YOUR own UNCENSORED AI & Use it for Hacking | Install private Ollama models in cloud, bypass most AI refusals | https://zsecurity.org/run-your-own-uncensored-ai-use-it-for-hacking/ |
| Feb 19, 2026 | Build Your Own AI HACKER with OpenClaw & Kali Linux | Autonomous AI hacking rig; OpenClaw + Kali; Nmap/Metasploit integration | https://zsecurity.org/build-your-own-ai-hacker-with-openclaw-kali-linux/ |

**February 2026 tutorial — "Build Your Own AI HACKER with OpenClaw & Kali Linux":**
- Demonstrates building a fully autonomous AI hacking agent ("Neo") using **OpenClaw** on Kali Linux in the cloud
- Connects AI "brain" to Claude 4.6 Opus or DeepSeek via OpenRouter
- Installs Kali tools; agent has direct access to **Nmap**, **Metasploit**, web browser
- Uses **ClawHub** skills: `prompt-guard`, `stealth-browser`, `tavily-search-pro`
- Configures agent to report back to phone; passes rules to subagents; updates AGENTS.md
- Principle: "Be proactive, obey user, try everything to achieve goals"

**Note on OpenClaw:** OpenClaw (also called MoltBot) is an autonomous AI assistant that can execute tasks, access local files, and authenticate to internal systems — a key tool featured in both the zSecurity tutorial and the February 2026 red team study involving 38 researchers (Northeastern, Harvard, MIT, CMU).

### Hacking Masterclass Course
- Ever-evolving subscription course including AI hacking modules
- New monthly lessons on latest hacking trends
- 1 hour/month live class with Zaid on latest techniques
- Covers: AI for hacking, hack AI systems, uncensored AI deployment

---

## 4. BASI Group / BT6 / AI Hacking Community

### BT6 (Break The 6th)
- **Website:** https://bt6.gg
- **Description:** "An elite AI hacker collective led by Pliny the Liberator, the anonymous researcher infamous for breaking every frontier model within hours of release."
- **Structure:** 28 operators across two cohorts; third cohort in progress (December 2025)
- **Co-leadership:** Pliny the Liberator + John V ([@JohnVersus](https://x.com/JohnVersus))
- **Ethos:** Radical transparency, open-source focus — "if you can't open-source the data, we're not interested"
- **Vetting:** Skill AND integrity; white-hat only
- **Focus areas:** AI security, swarm intelligence, blockchain, robotics
- **Activities as of Q1 2026:** Weekly jailbreak demos on latest models (e.g., ChatGPT latest, March 2026), ongoing research, community challenges

### BASI Discord Community
- **Invite:** https://discord.gg/basi
- Created by Elder-Plinius
- 20,000+ members (TIME, August 2025) → 40,000+ members (Latent Space, December 2025)
- Members share new jailbreaking payloads, workshopping approaches
- Multiple AI companies and organizations are known to monitor the Discord

### BASI-LABS GitHub Organization
- **URL:** https://github.com/BASI-LABS
- Repositories: `parseltongue` (browser extension for tokenization/encoding), computer_use fork, ai-toolkit fork, flux fork, bounties tracker

### Notable AI Bounty / Bug Disclosures

While BT6 does not publicly disclose specific bug bounties (often declining closed bounties like Anthropic's $30k Constitutional AI challenge), adjacent community findings include:
- Pliny's real-time jailbreaks of every major model hours after release (documented across X)
- CL4R1T4S system prompt extractions from GPT-5 (August 2025), Cursor, Devin, Replit, Manus, etc.
- Segmented sub-agent attack (weaponizing Claude orchestrators) — predicted by Pliny 11 months before Anthropic's official disclosure
- BT6 participates in AI purple-teaming competitions (Pliny, Feb 12, 2026: gamified 1v1/2v2 AI purple-teaming format)

---

## 5. Other Notable AI Red Teamers to Track in 2026

### Johann Rehberger (@wunderwuzzi) — "Embrace The Red"
- **Blog:** https://embracethered.com/blog/
- **Focus:** Prompt injection in deployed AI systems — agentic AI, coding agents, browser agents
- **Major contribution:** "The Month of AI Bugs" (August 2025) — published one critical AI vulnerability per day across major AI platforms for 31 days straight, exposing systemic vulnerabilities across ChatGPT, Google Jules, and every major AI system in production ([EC-Council writeup](https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/what-is-prompt-injection-in-ai-real-world-examples-and-prevention-tips/))
- **Key findings:**
  - ChatGPT Azure backdoor: domain allow-listing bypass via `*.blob.core.windows.net` enabling Markdown-based memory exfiltration
  - Google Jules: complete AI kill chain — from prompt injection to full remote control ("unrestricted outbound internet connectivity")
  - **SpAIware (September 2024):** First demonstration that ChatGPT's memory feature could be exploited for continuous data exfiltration via indirect prompt injection in documents/web pages
  - Devin AI: $500 subscription, GitHub issue with hidden prompt → full agent compromise ([Sysid, February 2026](https://sysid.github.io/your-agent-has-root/))
- **Recent talk:** "Exploiting AI Computer-Use and Coding Agents with Prompt Injections" (February 24, 2026) — [YouTube](https://www.youtube.com/watch?v=qTZT2gxscpc) — covers computer-use agents, coding copilots, local dev assistants, AI Kill Chain demos
- **Key concept:** **AI memory poisoning / "spyware" model** — planting malicious instructions into persistent AI memory for cross-session persistence

### Sander Schulhoff — HackAPrompt / LearnPrompting
- **Substack:** https://sanderschulhoff.substack.com/
- **HackAPrompt platform:** First-ever crowdsourced AI red-teaming evaluation (like LMArena, but for security)
- **Community:** 50,000+ members
- **Notable paper:** Co-authored with OpenAI, Google DeepMind, and Anthropic researchers — "The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections" (October 2025, arXiv):
  - Tested 12 published defenses with adaptive attacks (gradient descent, RL, random search, human-guided)
  - **Bypassed all 12 defenses with >90% attack success rate** — despite most originally reporting near-zero success rates
  - Human red-team setting scored **100%** — defeating every defense
  - Conclusion: Static evaluation of AI defenses is fundamentally inadequate
- **December 2025 post:** ["The AI Security Industry is Bullshit"](https://sanderschulhoff.substack.com/p/the-ai-security-industry-is-bullshit) — argues that 2,000+ automated red-teaming systems all work against any defense; the real problem is adaptive evaluation
- **Lenny's Newsletter interview:** ["The coming AI security crisis"](https://www.lennysnewsletter.com/p/the-coming-ai-security-crisis) (December 2025) — discusses why we haven't had a major AI security incident yet (agents not powerful enough), but why it's coming

### Simon Willison
- **Blog:** https://simonwillison.net
- **Key concepts:**
  - **"The Lethal Trifecta"** — coined the term for the three capabilities that create catastrophic risk: access to private data + exposure to untrusted content + external communication ability
  - Active tracker of all major prompt injection vulnerability disclosures
- **2026 predictions post:** [LLM Predictions for 2026](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/) (January 8, 2026) — predicts a "prompt injection worm" that infects Python/NPM packages; highlights sandboxing (containers, WebAssembly) as the path forward
- **November 2025 post:** [New prompt injection papers: Agents Rule of Two and The Attacker Moves Second](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/) — covers Meta's Agents Rule of Two and the Schulhoff adaptive attacks paper

### Mick Ayzenberg (Meta AI Security)
- **Role:** Security Tech Lead @ Meta — AI Agent Security
- **Key contribution:** Meta's **"Agents Rule of Two"** framework (October 31, 2025, Meta AI Blog) — proposes that AI agents must satisfy no more than **two** of these three properties to avoid catastrophic prompt injection consequences:
  - [A] Can process untrustworthy inputs
  - [B] Has access to sensitive systems or private data
  - [C] Can change state or communicate externally
- Framework builds on Willison's "Lethal Trifecta" and Google Chrome's Rule of 2 for memory safety

### Thomas Roccia (Microsoft Threat Intelligence)
- **Tool released 2026:** **NOVA** — Prompt pattern matching tool (like YARA for malware, but for detecting malicious/suspicious LLM prompts)
  - Supports: prompt hunting, LLM guardrail enforcement, logging attack attempts
  - MCP server integration — stops execution on rule match, logs all matches
  - Featured in Jason Haddix's February 2026 newsletter as a breakout tool

---

## 6. Notable Open-Source AI Security Projects (2026)

| Tool | Creator | Description | URL |
|---|---|---|---|
| **Augustus** | Praetorian (12 Caesars Campaign) | Open-source LLM vulnerability scanner; 210+ probes across 47 attack categories (jailbreaks, prompt injection, adversarial examples, data extraction, agent attacks); 28 provider support; single Go binary | https://www.praetorian.com/blog/introducing-augustus-open-source-llm-prompt-injection/ |
| **Julius** | Praetorian (12 Caesars Campaign) | HTTP-based LLM service fingerprinting; identifies shadow AI deployments | https://github.com/praetorian-inc/julius |
| **Garak** v0.14.0 | NVIDIA | LLM vulnerability scanner; static, dynamic, and adaptive probes; latest release February 4, 2026 | https://github.com/NVIDIA/garak |
| **Promptfoo** | Promptfoo (acquired by OpenAI, March 9, 2026) | AI security platform; automated red-teaming for GenAI apps; 50+ vulnerability types; trusted by 127 Fortune 500 companies | https://www.promptfoo.dev |
| **NOVA** | Thomas Roccia / Microsoft | YARA-like prompt pattern matching for LLM threat detection; MCP server integration | (via Haddix newsletter Feb 2026) |
| **burp-ai-agent** | six2dez | Adds MCP tooling to Burp Suite; connects Claude/Codex/Gemini/Ollama to drive Burp autonomously | (via Haddix newsletter Feb 2026) |
| **Parseltongue** | BASI-LABS / Elder-Plinius | Browser extension for real-time tokenization visualization and payload encoding | https://github.com/BASI-LABS/parseltongue |
| **PyRIT** | Microsoft | AI Red Teaming open-source framework; integrated into Arcanum's resource hub | (via arcanum-sec.github.io) |
| **Basilisk** | Open-source | AI red teaming and LLM security testing framework; GitHub Actions integration | https://github.com/marketplace/actions/basilisk-ai-security-scan |
| **OpenClaw** | (see below) | Autonomous AI assistant for executing tasks, file access, shell commands; used in red team research and by zSecurity | Featured in 38-researcher study, Feb 2026 |

**Note on Promptfoo/OpenAI acquisition (March 9, 2026):** OpenAI acquired Promptfoo to integrate security and safety testing natively into OpenAI Frontier platform. Promptfoo will remain open source. Key quote from acquisition: "Security testing built into the platform: Automated security testing and red-teaming capabilities will become a native part of the Frontier platform." ([OpenAI announcement](https://openai.com/index/openai-to-acquire-promptfoo/))

**Note on Praetorian's "12 Caesars" campaign:** Praetorian is open-sourcing one new AI attack tool per week for 12 weeks starting early 2026. Julius (LLM fingerprinting) and Augustus (210+ probe LLM scanner) are the first two released.

---

## 7. Key Landscape Shifts as of March 2026

1. **Agentic AI is the primary attack surface.** The field has moved from model-level jailbreaks to system-level attacks on AI agents with tool access. The 38-researcher study (Northeastern/Harvard/MIT/CMU, February 2026) showed agents comply with identity-spoofed requests, leak private data, and can be trapped in resource-burning loops.

2. **Prompt injection is officially unsolvable by current architecture.** OpenAI admitted in December 2025 that prompt injection "is unlikely to ever be fully 'solved'" — backed by UK NCSC. The Schulhoff et al. paper (October 2025) showed adaptive attacks bypass all known defenses with >90% success.

3. **Memory poisoning is the new frontier.** Rehberger's "SpAIware" → Radware's "ZombieAgent" (January 2026) → LayerX "Tainted Memories" (late 2025) — persistent memory injection is now a documented, working attack class against deployed AI systems.

4. **AI tools for offenders are maturing.** OpenClaw, burp-ai-agent, Augustus, and the Claude Code hackbot ecosystem demonstrate that AI-augmented offensive security tooling is production-ready in 2026.

5. **Academic research is catching up to the hacker community.** Papers now cite L1B3RT4S, Pliny, and BASI directly; automated investigator models attempt to replicate manual jailbreaks. The "Pliny Jailbreak" is a named object of study.

6. **The Promptfoo acquisition signals AI security going enterprise.** OpenAI buying a red teaming platform means AI security tooling is becoming infrastructure-level rather than niche.

---

## Summary: Key Links Reference

| Figure/Resource | Primary Link |
|---|---|
| Pliny the Liberator (X) | https://x.com/elder_plinius |
| Pliny website | https://pliny.gg |
| L1B3RT4S repo | https://github.com/elder-plinius/L1B3RT4S |
| CL4R1T4S repo | https://github.com/elder-plinius/CL4R1T4S |
| P4RS3LT0NGV3 tool | https://elder-plinius.github.io/P4RS3LT0NGV3/ |
| P4RS3LT0NGV3 repo | https://github.com/elder-plinius/P4RS3LT0NGV3 |
| BASI Discord | https://discord.gg/basi |
| BT6 | https://bt6.gg |
| BASI-LABS GitHub | https://github.com/BASI-LABS |
| Jason Haddix (X) | https://x.com/Jhaddix |
| Arcanum Security | https://arcanum-sec.com |
| Arcanum PI Taxonomy | https://arcanum-sec.github.io/arc_pi_taxonomy/ |
| Arcanum AI Resource Hub | https://arcanum-sec.github.io/ai-sec-resources/ |
| ExecutiveOffense newsletter | https://executiveoffense.beehiiv.com |
| Hackbots course | https://www.arcanum-sec.com/training/hackbots |
| Attacking AI course | https://arcanum-sec.com/training/attacking-ai |
| zSecurity | https://zsecurity.org |
| zSecurity Masterclass | https://zsecurity.org/courses/masterclass-membership/ |
| Johann Rehberger (blog) | https://embracethered.com/blog/ |
| Sander Schulhoff (substack) | https://sanderschulhoff.substack.com/ |
| Simon Willison (blog) | https://simonwillison.net |
| Garak (NVIDIA) | https://github.com/NVIDIA/garak |
| Promptfoo | https://www.promptfoo.dev |
| Praetorian 12 Caesars (Augustus) | https://www.praetorian.com/blog/introducing-augustus-open-source-llm-prompt-injection/ |
| Parseltongue (BASI) | https://github.com/BASI-LABS/parseltongue |
| Latent Space Podcast (Pliny) | https://www.latent.space/p/jailbreaking-agi-pliny-the-liberator |
| TIME 100 AI: Pliny | https://time.com/collections/time100-ai-2025/7305870/pliny-the-liberator/ |
| Promptfoo OpenAI acquisition | https://openai.com/index/openai-to-acquire-promptfoo/ |
