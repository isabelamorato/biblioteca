# Skills Recommendations

Skills are packaged expertise with workflows, reference materials, and best practices.

## Available from Official Plugins

| Plugin | Skills |
|--------|--------|
| **plugin-dev** | skill-development, hook-development, command-development, agent-development |
| **commit-commands** | commit, commit-push-pr |
| **frontend-design** | frontend-design |
| **hookify** | writing-rules |
| **feature-dev** | feature-dev |

## Custom Skill Patterns

| Codebase Signal | Skill to Create | Invocation |
|-----------------|-----------------|------------|
| API routes | **api-doc** (with OpenAPI template) | Both |
| Database project | **create-migration** (with validation script) | User-only |
| Test suite | **gen-test** (with example tests) | User-only |
| Component library | **new-component** (with templates) | User-only |
| PR workflow | **pr-check** (with checklist) | User-only |
| Releases | **release-notes** (with git context) | User-only |
| Code style | **project-conventions** | Claude-only |
| Onboarding | **setup-dev** (with prereq script) | User-only |

## Invocation Control

| Setting | User | Claude | Use for |
|---------|------|--------|---------|
| (default) | ✓ | ✓ | General-purpose skills |
| `disable-model-invocation: true` | ✓ | ✗ | Side effects (deploy, send) |
| `user-invocable: false` | ✗ | ✓ | Background knowledge |

## Dynamic Context Injection

Use `` !`command` `` in SKILL.md to inject live data before the skill runs.
