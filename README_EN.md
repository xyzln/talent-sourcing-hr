<div align="center">

<img src="assets/hero-agent-temp-worker.jpg" width="760" alt="Agent's HR"/>

# Agent's HR · Agent Architect

### Don't know how to create an agent? Can't spawn sub-agents?
**Study how the real-world role is designed, translate the job design into agent persona and skills, and generate the matching agent.**

<p>
  <img src="https://img.shields.io/badge/version-1.1.0-0d9488?style=flat-square" alt="version"/>
  <img src="https://img.shields.io/badge/license-MIT-2563eb?style=flat-square" alt="license MIT"/>
  <img src="https://img.shields.io/badge/languages-5-7c3aed?style=flat-square" alt="5 languages"/>
  <img src="https://img.shields.io/badge/platform-WorkBuddy%20Expert-0f766e?style=flat-square" alt="platform"/>
  <img src="https://img.shields.io/badge/SkillHub-published-f59e0b?style=flat-square" alt="SkillHub"/>
</p>

</div>

---

## 📖 Table of Contents

- [Why you need it](#why-you-need-it)
- [Core capabilities](#core-capabilities)
- [Five-step workflow](#five-step-workflow)
- [Coverage scoring](#coverage-scoring)
- [Quick start](#quick-start)
- [Usage examples](#usage-examples)
- [Language versions](#language-versions)
- [Compliance](#compliance)
- [Repository structure](#repository-structure)
- [License](#license)

---

## Why you need it

Want to build an agent (or a sub-agent, or a skill) but have no idea how to design it - so you let a generic agent guess? Agent's HR runs on a single principle: **never design an agent from scratch - first study how the people who do this job in the real world are designed**. Responsibilities, requirements, workflows, collaboration interfaces, and KPIs all get researched, then the job design is translated item by item into an agent design, producing a spec you can actually ship.

| Pain point | What a generic agent does | What Agent's HR does |
|:---|:---|:---|
| Don't know how to create an agent / sub-agent | Writes prompts by feel, hopes for the best | Studies how the real-world role is designed, then generates the agent |
| Design without evidence | Invents persona and skills out of thin air | Every design decision traces back to job-design research (source + date) |
| Misses job elements | Writes whatever comes to mind | Six-element checklist: responsibilities / requirements / workflow / collaboration / KPIs / toolstack |
| No quality gate | "Looks usable" | 0-5 coverage anchors + weighted scoring + hard veto |
| Never ships | Advice only, no spec | Full agent spec + landing form and activation steps |

---

## Core capabilities

| # | Capability | Description |
|:--|:---|:---|
| 1 | **Real-world job design research** | Web-wide research on how the role is designed: responsibilities from real JDs, requirements, daily workflow, collaboration interfaces, KPIs, toolstack; cross-validated across sources, honestly reports when nothing is found |
| 2 | **Job → agent mapping** | Translates six job elements into agent design elements: role positioning → persona, responsibilities → skills & workflow, requirements → capability anchors & guardrails, collaboration → I/O spec, KPIs → acceptance criteria, toolstack → tool list |
| 3 | **Coverage scoring** | 5-8 design dimensions scored on 0-5 anchors, weighted via `match_score.py`; outputs coverage grade, strong-coverage items, gap items, and veto flags |
| 4 | **Agent spec generation** | Conclusion-first full spec (frontmatter, persona, skills, workflow, tools, guardrails, acceptance criteria) plus the landing form (expert package / standalone skill / sub-agent) and activation steps |

---

## Five-step workflow

<img src="assets/workflow_EN.svg" width="100%" alt="Five-step workflow"/>

| Step | Input | Output |
|:--|:---|:---|
| 1. Clarify needs | The user's agent idea | Four questions: purpose / scenario / landing form / boundaries |
| 2. Study job design | Needs | Six-element research summary + sources and dates |
| 3. Map to agent | Job design summary | Design draft (persona / skills / workflow / tools / boundaries) |
| 4. Score coverage | Design draft + job evidence | Coverage total + grade + gap items and fix suggestions |
| 5. Generate spec | All results | Full agent spec + landing form and activation steps |

---

## Coverage scoring

Scores are based on job-design research evidence only; no evidence, no score. Weighted average × 20 = coverage percentage:

| Coverage | Grade | Action |
|:--|:---|:---|
| ≥ 85 | **A · Ship it** | Build directly as expert package / skill / sub-agent per the spec |
| 70 – 84 | **B · Basically usable** | Ship while closing gap items (more research or more design) |
| 50 – 69 | **C · Has gaps** | Finish research or design first, then ship |
| < 50 | **D · Mismatch** | Go back to step 2 and re-research the role |
| Core item ≤ 2 | **Hard veto** | Default D regardless of total, unless the requester explicitly waives |

---

## Quick start

### Option 1: Install as an expert package (recommended)

Install this repository as a WorkBuddy expert package:

```bash
# Clone the repo
git clone https://github.com/xyzln/talent-sourcing-hr.git

# Copy to the experts directory
cp -r talent-sourcing-hr ~/.workbuddy/plugins/marketplaces/my-experts/plugins/

# Register (script lives in the expert-manager skill's scripts/ directory)
python3 register_expert.py ~/.workbuddy/plugins/marketplaces/my-experts/plugins/talent-sourcing-hr
```

Then pick **Agent's HR** in the WorkBuddy expert center and describe the agent you want to build.

### Option 2: Use the skill standalone

The `skills/recruit-web-sourcing/` directory can be copied to `~/.workbuddy/skills/` for standalone use, or install a language version from SkillHub by searching `recruit-web-sourcing`.

---

## Usage examples

> Don't know how to create an agent or spawn sub-agents? I want this agent to "analyze user behavior and output actionable conclusions" - research how the real-world role is designed and generate the agent directly.

> Research how a "data analyst" is designed in the real world: responsibilities, requirements, workflow, collaboration interfaces, and KPIs.

> Translate this job design into an agent spec: persona, skills, tools, workflow, and guardrails.

---

## Language versions

| Language | README | SkillHub skill |
|:---|:---|:---|
| 🇨🇳 简体中文 | [README_CN.md](README_CN.md) | `recruit-web-sourcing-cn` |
| 🇹🇼 繁體中文 | [README_TW.md](README_TW.md) | `recruit-web-sourcing-tw` |
| 🇬🇧 English | [README_EN.md](README_EN.md) | `recruit-web-sourcing-en` |
| 🇷🇺 Русский | [README_RU.md](README_RU.md) | `recruit-web-sourcing-ru` |
| 🇸🇦 العربية | [README_AR.md](README_AR.md) | `recruit-web-sourcing-ar` |

Each language version fully translates SKILL.md, the three reference manuals, and the scoring script's output text.

---

## Compliance

- Job-design research uses **publicly available sources only**; every conclusion carries its source and retrieval date - nothing is fabricated
- **No agents designed for cheating, fraud, discrimination, regulatory evasion, or privacy violations**
- Every agent design element must trace back to job-design research; no invented capabilities
- Coverage scores are evidence-based only; no evidence = 0 points, marked "to be verified"

---

## Repository structure

```text
talent-sourcing-hr/
├── README.md                        # Entry point (language switcher)
├── README_CN.md / _TW / _EN / _RU / _AR   # Five language landing pages
├── assets/                          # Illustrations
│   ├── hero-agent-temp-worker.jpg   # Persona hero art
│   ├── talent-sourcing-network.jpg  # Job-design research concept art
│   └── workflow_{CN,TW,EN,RU,AR}.svg      # Five-step workflow diagram (5 languages)
├── .codebuddy-plugin/plugin.json    # Expert package manifest
├── agents/talent-sourcing-hr.md     # Expert persona (Agent's HR · Gu Xun)
├── avatars/expert.png               # Expert avatar
├── skills/recruit-web-sourcing/     # Skill source (Simplified Chinese)
│   ├── SKILL.md
│   ├── references/                  # Job-design research playbook / mapping model / spec template
│   └── scripts/match_score.py       # Coverage calculator
├── i18n/{CN,TW,EN,RU,AR}/           # Full skill versions in five languages
└── LICENSE
```

---

## License

[MIT](LICENSE) © 2026 talent-sourcing-hr contributors

<div align="center">

**⭐ Star this repo so more people who don't know how to build agents can find Agent's HR**

</div>
