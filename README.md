# AI Mastery — Claude Curriculum

**Profile:** Developer / engineer · Python · All surfaces (claude.ai, Claude Code, API, Cowork)
**Session length:** 30 minutes · Near-daily cadence
**Format:** Mixed — concept+demo, explain→try→critique, project-based
**Status:** Living document — updated as new Claude features launch

---

## Repo Structure

```
ai_mastery/
├── README.md                  ← this curriculum
├── sessions/
│   ├── 01-how-claude-works/
│   │   ├── notes.md
│   │   └── demo.py
│   ├── 02-prompt-architecture/
│   └── ...
├── projects/                  ← capstone builds (Sessions 39–43)
└── resources.md               ← audited links per session
```

Each session gets its own folder: notes, code, and validated resources.

---

## How Sessions Work

Each 30-min session follows this structure:

| Time | Activity |
|------|----------|
| 0–5 min | Context and goal for today |
| 5–20 min | Core content (format varies) |
| 20–28 min | Apply or critique |
| 28–30 min | One takeaway + what's next |

**To start:** "Let's do Session [#]" or "Next session."
**To go deeper mid-session:** "Go deeper on this."
**New features:** Flagged by Claude when worth learning — new lesson slot proposed.

---

## TIER 1 — Foundations with Depth

> Even experienced users have gaps here. Establishes the mental model everything else builds on.

| # | Session | Format | Surface |
|---|---------|--------|---------|
| 01 | How Claude actually works — models, context windows, tokens, and what "thinking" means | Concept + demo | claude.ai |
| 02 | Prompt architecture — system prompts, roles, and why structure matters more than wording | Explain → try → critique | claude.ai |
| 03 | The Anthropic API deep dive — authentication, request anatomy, response parsing in Python | Project-based | API |
| 04 | Model selection — Opus vs Sonnet vs Haiku, when to use which, cost/latency tradeoffs | Concept + demo | API |
| 05 | Context window management — what goes in, what gets cut, how to design around limits | Explain → try → critique | API |
| 06 | Temperature, top-p, and sampling — what they actually do vs. the myths | Concept + demo | API |

---

## TIER 2 — Prompting Mastery

> The difference between getting an answer and getting the right answer, reliably.

| # | Session | Format | Surface |
|---|---------|--------|---------|
| 07 | System prompt engineering — building a reusable persona and instruction layer | Project-based | API + claude.ai |
| 08 | Chain-of-thought and structured reasoning — when to force it, when to let it run | Explain → try → critique | claude.ai |
| 09 | XML tags, delimiters, and structured inputs — Claude's native language | Concept + demo | API |
| 10 | Few-shot prompting in Python — building dynamic example injection | Project-based | API |
| 11 | Prompt chaining — designing multi-step pipelines that don't break | Project-based | API |
| 12 | Output formatting control — JSON, markdown, custom schemas, schema enforcement | Explain → try → critique | API |

---

## TIER 3 — Claude Code Mastery

> Claude Code is its own discipline. These sessions treat it seriously.

| # | Session | Format | Surface |
|---|---------|--------|---------|
| 13 | Claude Code setup, config, and mental model — what it is vs. a chatbot | Concept + demo | Claude Code |
| 14 | Your first real Claude Code session — navigating a codebase, asking the right questions | Explain → try → critique | Claude Code |
| 15 | CLAUDE.md — writing a project brief that makes Claude Code dramatically more useful | Project-based | Claude Code |
| 16 | Agentic loops in Claude Code — letting it run, reviewing diffs, safe interruption | Concept + demo | Claude Code |
| 17 | Claude Code + Git — commit discipline, branch strategy, reviewing AI-generated code | Project-based | Claude Code |
| 18 | Debugging with Claude Code — feeding errors, stack traces, and iterating fast | Explain → try → critique | Claude Code |
| 19 | Claude Code for refactoring — systematic improvement without breaking things | Project-based | Claude Code |
| 20 | MCP servers in Claude Code — connecting external tools to your dev workflow | Concept + demo | Claude Code |

---

## TIER 4 — Tool Use & Agentic Systems

> Building Claude into things that actually do work autonomously.

| # | Session | Format | Surface |
|---|---------|--------|---------|
| 21 | Tool use fundamentals — function calling, JSON schemas, Python integration | Concept + demo | API |
| 22 | Building your first tool-using agent in Python | Project-based | API |
| 23 | Multi-tool orchestration — giving Claude a toolkit and letting it choose | Project-based | API |
| 24 | Human-in-the-loop design — when to pause, confirm, and resume | Explain → try → critique | API |
| 25 | Error handling in agentic flows — retries, fallbacks, graceful degradation | Project-based | API |
| 26 | MCP deep dive — what it is, why it matters, building your own MCP server in Python | Concept + demo | API + Claude Code |

---

## TIER 5 — Cowork & Automation

> claude.ai's power-user and automation layer — Files, Projects, Cowork, integrations.

| # | Session | Format | Surface |
|---|---------|--------|---------|
| 27 | Projects in claude.ai — knowledge bases, persistent context, and when to use them | Concept + demo | claude.ai |
| 28 | Cowork fundamentals — what it automates, how to set tasks up for success | Explain → try → critique | Cowork |
| 29 | Cowork for file and task automation — real workflows, not toy examples | Project-based | Cowork |
| 30 | Google Drive + Gmail + Calendar via MCP — building a connected personal assistant | Project-based | claude.ai + MCP |
| 31 | Designing repeatable workflows — prompts as templates, automation as a system | Project-based | All |
| 32 | Claude in the browser (Chrome extension) — live web research and action patterns | Concept + demo | claude.ai |

---

## TIER 6 — Advanced API Patterns

> Production-grade usage: streaming, batching, cost control, evals.

| # | Session | Format | Surface |
|---|---------|--------|---------|
| 33 | Streaming responses in Python — real-time output, progress feedback, UX patterns | Project-based | API |
| 34 | Batch API — async jobs, cost savings, when batch beats real-time | Concept + demo | API |
| 35 | Building an eval harness — testing your prompts like you test your code | Project-based | API |
| 36 | Cost monitoring and optimization — token budgeting, caching, model routing | Explain → try → critique | API |
| 37 | Prompt caching — what it is, how to structure prompts to hit cache, savings math | Concept + demo | API |
| 38 | Rate limits and retry logic — production-safe Python patterns | Project-based | API |

---

## TIER 7 — Capstone Projects

> Each session builds something real that you keep.

| # | Session | Format | Surface |
|---|---------|--------|---------|
| 39 | Build: Personal AI assistant with memory (Projects + API) | Project-based | All |
| 40 | Build: Python CLI tool powered by Claude | Project-based | API + Claude Code |
| 41 | Build: Automated document pipeline (intake → process → output) | Project-based | Cowork + API |
| 42 | Build: Claude-powered research agent with web search + tools | Project-based | API |
| 43 | Build: Your own MCP server connecting Claude to something you actually use | Project-based | Claude Code + API |

---

## 🔄 Living Additions

> Flagged by Claude when a new feature clears the bar for your goals.

| # | Session | Status |
|---|---------|--------|
| L1 | *(reserved — next major Claude model release)* | Pending |
| L2 | *(reserved — new Cowork features)* | Pending |
| L3 | *(reserved — Claude Code updates)* | Pending |

---

## Progress Tracker

| Tier | Sessions | Done |
|------|----------|------|
| Tier 1 — Foundations | 01–06 | 0/6 |
| Tier 2 — Prompting | 07–12 | 0/6 |
| Tier 3 — Claude Code | 13–20 | 0/8 |
| Tier 4 — Tool Use & Agents | 21–26 | 0/6 |
| Tier 5 — Cowork & Automation | 27–32 | 0/6 |
| Tier 6 — Advanced API | 33–38 | 0/6 |
| Tier 7 — Capstone Projects | 39–43 | 0/5 |
| **Total** | | **0/43** |

---

*Last updated: 2026-05-04*
