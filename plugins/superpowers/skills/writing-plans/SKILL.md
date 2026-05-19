---
name: writing-plans
description: Use when you have a spec or requirements for a multi-step task, before touching code
---

# Writing Plans

**Announce at start:** "I'm using the writing-plans skill to create the implementation plan."

**Save plans to:** `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`

## Plan Document Header

Every plan MUST start with:

```markdown
# [Feature Name] Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

## Task Structure

Each task contains: Files (create/modify/test), TDD steps (failing test → run → implement → run → commit).

**Bite-sized steps (2-5 minutes each):** "Write the failing test" is a step. "Run it" is a step.

## No Placeholders

These are plan failures - never write them:
- "TBD", "TODO", "implement later"
- "Add appropriate error handling"
- "Write tests for the above" (without actual test code)
- Steps that describe what to do without showing how

## Self-Review

After writing complete plan:
1. Spec coverage: Can you point to a task for each requirement?
2. Placeholder scan: Any TBD/TODO patterns?
3. Type consistency: Do method signatures match across tasks?

## Execution Handoff

After saving, offer:
1. **Subagent-Driven (recommended)** - Uses superpowers:subagent-driven-development
2. **Inline Execution** - Uses superpowers:executing-plans
