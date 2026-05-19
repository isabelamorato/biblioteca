---
name: dispatching-parallel-agents
description: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
---

# Dispatching Parallel Agents

## Overview

Delegate tasks to specialized agents with isolated context. When you have multiple unrelated failures (different test files, different subsystems, different bugs), investigate them in parallel.

**Core principle:** Dispatch one agent per independent problem domain. Let them work concurrently.

## When to Use

**Use when:**
- 3+ test files failing with different root causes
- Multiple subsystems broken independently
- Each problem can be understood without context from others
- No shared state between investigations

**Don't use when:**
- Failures are related (fix one might fix others)
- Need to understand full system state
- Agents would interfere with each other

## The Pattern

1. **Identify Independent Domains** — group failures by what's broken
2. **Create Focused Agent Tasks** — each agent gets: specific scope, clear goal, constraints, expected output
3. **Dispatch in Parallel** — all Task calls concurrently
4. **Review and Integrate** — read summaries, verify no conflicts, run full test suite

## Agent Prompt Structure

Good agent prompts are:
1. **Focused** - One clear problem domain
2. **Self-contained** - All context needed to understand the problem
3. **Specific about output** - What should the agent return?

## Common Mistakes

- **Too broad:** "Fix all the tests" - agent gets lost
- **No context:** Agent doesn't know where the problem is
- **No constraints:** Agent might refactor everything
- **Vague output:** You don't know what changed

## Verification

After agents return:
1. **Review each summary** - Understand what changed
2. **Check for conflicts** - Did agents edit same code?
3. **Run full suite** - Verify all fixes work together
4. **Spot check** - Agents can make systematic errors
