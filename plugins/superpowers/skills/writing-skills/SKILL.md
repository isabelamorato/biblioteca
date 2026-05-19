---
name: writing-skills
description: Use when creating new skills, editing existing skills, or verifying skills work before deployment
---

# Writing Skills

**Writing skills IS Test-Driven Development applied to process documentation.**

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

**REQUIRED BACKGROUND:** You MUST understand superpowers:test-driven-development before using this skill.

## TDD Mapping for Skills

| TDD Concept | Skill Creation |
|-------------|----------------|
| Test case | Pressure scenario with subagent |
| Production code | Skill document (SKILL.md) |
| Test fails (RED) | Agent violates rule without skill |
| Test passes (GREEN) | Agent complies with skill present |
| Refactor | Close loopholes while maintaining compliance |

## SKILL.md Structure

Frontmatter: `name` and `description` (max 1024 chars total). Description starts with "Use when..." and describes ONLY triggering conditions - NEVER summarize the skill's process.

## Claude Search Optimization (CSO)

**Critical:** Description = When to Use, NOT What the Skill Does

```yaml
# ❌ BAD: Summarizes workflow
description: Use when executing plans - dispatches subagent per task with code review

# ✅ GOOD: Just triggering conditions
description: Use when executing implementation plans with independent tasks in the current session
```

**Why this matters:** When a description summarizes workflow, Claude may follow the description instead of reading the full skill content.

## The Iron Law

```
NO SKILL WITHOUT A FAILING TEST FIRST
```

**RED Phase:** Run pressure scenario WITHOUT skill - document baseline behavior verbatim
**GREEN Phase:** Write minimal skill addressing those specific failures. Verify agents now comply.
**REFACTOR Phase:** Find new rationalizations, add explicit counters, re-test until bulletproof.

## Common Rationalizations for Skipping Testing

| Excuse | Reality |
|--------|--------|
| "Skill is obviously clear" | Clear to you ≠ clear to other agents. Test it. |
| "Testing is overkill" | Untested skills have issues. Always. |
| "No time to test" | Deploying untested skill wastes more time fixing it later. |

**All of these mean: Test before deploying. No exceptions.**
