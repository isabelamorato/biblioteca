# Hooks Recommendations

Hooks automatically run commands in response to Claude Code events. They're ideal for enforcement and automation that should happen consistently.

## Auto-Formatting Hooks

| Tool | Detection | Value |
|------|-----------|-------|
| Prettier | `.prettierrc`, `.prettierrc.json`, `prettier.config.js` | Code stays formatted without thinking about it |
| ESLint | `.eslintrc`, `.eslintrc.json`, `eslint.config.js` | Lint errors fixed automatically |
| Black/isort | `pyproject.toml` with black/isort | Consistent Python formatting |
| Ruff | `ruff.toml`, `pyproject.toml` with `[tool.ruff]` | Fast, comprehensive Python linting |
| gofmt | `go.mod` | Standard Go formatting |
| rustfmt | `Cargo.toml` | Standard Rust formatting |

## Type Checking Hooks

| Tool | Detection | Value |
|------|-----------|-------|
| TypeScript | `tsconfig.json` | Catch type errors immediately |
| mypy/pyright | `mypy.ini`, `pyrightconfig.json` | Catch type errors in Python |

## Protection Hooks

| Hook | When to use |
|------|-------------|
| Block .env edits | `.env`, `.env.local`, `credentials.json` present |
| Block lock file edits | `package-lock.json`, `yarn.lock`, `Cargo.lock` present |

## Test Runner Hooks

| Tool | Detection |
|------|-----------|
| Jest | `jest.config.js`, `__tests__/`, `*.test.ts` |
| pytest | `pytest.ini`, `tests/`, `test_*.py` |

## Notification Hooks

| Matcher | Use Case |
|---------|----------|
| `permission_prompt` | Alert when Claude requests permissions |
| `idle_prompt` | Alert when Claude is waiting for input (60+ seconds) |
| `auth_success` | Authentication succeeds |
| `elicitation_dialog` | MCP tool needs input |

## Hook Placement

Hooks go in `.claude/settings.json`.
