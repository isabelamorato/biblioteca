---
name: claude-automation-recommender
description: Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.
tools: Read, Glob, Grep, Bash
---

# Claude Automation Recommender

Analyze codebase patterns to recommend tailored Claude Code automations across all extensibility options.

**This skill is read-only.** It analyzes the codebase and outputs recommendations. It does NOT create or modify any files.

## Output Guidelines

- **Recommend 1-2 of each type**: Don't overwhelm - surface the top 1-2 most valuable automations per category
- **If user asks for a specific type**: Focus only on that type and provide more options (3-5 recommendations)
- **Go beyond the reference lists**: Use web search to find recommendations specific to the codebase's tools
- **Tell users they can ask for more**: End by noting they can request more recommendations for any specific category

## Automation Types Overview

| Type | Best For |
|------|----------|
| **Hooks** | Automatic actions on tool events (format on save, lint, block edits) |
| **Subagents** | Specialized reviewers/analyzers that run in parallel |
| **Skills** | Packaged expertise, workflows, and repeatable tasks |
| **Plugins** | Collections of skills that can be installed |
| **MCP Servers** | External tool integrations (databases, APIs, browsers, docs) |

## Workflow

### Phase 1: Codebase Analysis

Gather project context to detect: language/framework, frontend stack, backend stack, database, external APIs, testing setup, CI/CD, issue tracking.

See [references/mcp-servers.md](references/mcp-servers.md), [references/hooks-patterns.md](references/hooks-patterns.md), [references/skills-reference.md](references/skills-reference.md), [references/subagent-templates.md](references/subagent-templates.md), [references/plugins-reference.md](references/plugins-reference.md) for detailed patterns.

### Phase 2: Generate Recommendations

Based on analysis, generate 1-2 recommendations per category most valuable for this specific codebase.

### Phase 3: Output Recommendations Report

Format: brief codebase profile, then one section per category (MCP Servers, Skills, Hooks, Subagents, Plugins) with only the most relevant recommendations.

End with: offer to help implement any recommendation.
