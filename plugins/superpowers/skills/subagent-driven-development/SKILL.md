---
name: subagent-driven-development
description: Use when executing implementation plans with independent tasks in the current session
---

# Subagent-Driven Development

Execute plan by dispatching fresh subagent per task, with two-stage review after each: spec compliance review first, then code quality review.

**Core principle:** Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration

## When to Use

- Have implementation plan? Yes
- Tasks mostly independent? Yes
- Stay in this session? Yes

If tasks are tightly coupled: Manual execution or brainstorm first. If parallel session preferred: executing-plans.

## The Process

1. Read plan, extract all tasks with full text, note context, create TodoWrite
2. Per task:
   a. Dispatch implementer subagent (see implementer-prompt.md)
   b. Answer any questions before they proceed
   c. Implementer implements, tests, commits, self-reviews
   d. Dispatch spec reviewer subagent (see spec-reviewer-prompt.md)
   e. If spec issues: implementer fixes, re-review
   f. Dispatch code quality reviewer subagent (see code-quality-reviewer-prompt.md)
   g. If quality issues: implementer fixes, re-review
   h. Mark task complete in TodoWrite
3. After all tasks: Dispatch final code reviewer for entire implementation
4. Use superpowers:finishing-a-development-branch

## Implementer Status Handling

- **DONE:** Proceed to spec compliance review
- **DONE_WITH_CONCERNS:** Read concerns before proceeding
- **NEEDS_CONTEXT:** Provide missing context and re-dispatch
- **BLOCKED:** Assess blocker: provide context, upgrade model, break task, or escalate to human

## Red Flags

**Never:**
- Start implementation on main/master without user consent
- Skip reviews (spec compliance OR code quality)
- Dispatch multiple implementation subagents in parallel (conflicts)
- Make subagent read plan file (provide full text instead)
- Accept "close enough" on spec compliance
- Start code quality review before spec compliance is ✅

## Integration

- **superpowers:using-git-worktrees** - REQUIRED: Set up isolated workspace before starting
- **superpowers:writing-plans** - Creates the plan this skill executes
- **superpowers:requesting-code-review** - Code review template for reviewer subagents
- **superpowers:finishing-a-development-branch** - Complete development after all tasks
