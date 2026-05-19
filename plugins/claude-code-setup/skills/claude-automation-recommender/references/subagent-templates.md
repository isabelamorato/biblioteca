# Subagent Recommendations

Subagents are specialized Claude instances that run in parallel, each with their own context window.

## Quick Reference: Detection → Recommendation

| If You See | Recommend Subagent |
|------------|-------------------|
| Large codebase (>500 files) | **code-reviewer** |
| Auth/payment code | **security-reviewer** |
| Few tests | **test-writer** |
| API routes | **api-documenter** |
| Database heavy | **performance-analyzer** |
| Frontend components | **ui-reviewer** |
| Outdated packages | **dependency-updater** |
| Old framework version | **migration-helper** |

## Subagent Profiles

| Subagent | Model | Tools | Best For |
|----------|-------|-------|----------|
| code-reviewer | sonnet | Read, Grep, Glob, Bash | Code quality, large codebases |
| security-reviewer | sonnet | Read, Grep, Glob (read-only) | OWASP vulnerabilities, auth issues |
| test-writer | sonnet | Read, Write, Grep, Glob | Generating tests matching conventions |
| api-documenter | sonnet | Read, Write, Grep, Glob | OpenAPI specs, endpoint docs |
| performance-analyzer | sonnet | Read, Grep, Glob, Bash | N+1 queries, O(n²) algorithms |
| ui-reviewer | sonnet | Read, Grep, Glob | Accessibility, UX, responsive design |
| dependency-updater | sonnet | Read, Write, Bash, Grep | Safe incremental dep updates |
| migration-helper | opus | Read, Write, Grep, Glob, Bash | Framework/version migrations |

## Subagent Placement

Subagents go in `.claude/agents/`.
