# Plugin Recommendations

Plugins are installable collections of skills, commands, agents, and hooks. Install via `/plugin install`.

## Official Plugins

| Plugin | Best For | Key Features |
|--------|----------|--------------|
| **plugin-dev** | Building Claude Code plugins | Skills for creating skills, hooks, commands, agents |
| **pr-review-toolkit** | PR review workflows | Specialized review agents |
| **code-review** | Automated code review | Multi-agent review with confidence scoring |
| **code-simplifier** | Code refactoring | Simplify code while preserving functionality |
| **feature-dev** | Feature development | End-to-end feature workflow |
| **commit-commands** | Git workflows | /commit, /commit-push-pr commands |
| **hookify** | Automation rules | Create hooks from conversation patterns |
| **frontend-design** | UI development | Production-grade UI, avoids generic aesthetics |
| **security-guidance** | Security awareness | Warns about security issues when editing |
| **typescript-lsp** | TypeScript/JavaScript | Language server integration |
| **pyright-lsp** | Python | Language server integration |

## Quick Reference: Codebase → Plugin

| Codebase Signal | Recommended Plugin |
|-----------------|-------------------|
| Building plugins | plugin-dev |
| PR-based workflow | pr-review-toolkit |
| Git commits | commit-commands |
| React/Vue/Angular | frontend-design |
| TypeScript project | typescript-lsp |
| Python project | pyright-lsp |
| Security-sensitive code | security-guidance |
