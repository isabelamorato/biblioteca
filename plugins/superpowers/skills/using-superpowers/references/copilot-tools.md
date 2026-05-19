# Copilot CLI Tool Mapping

Skills use Claude Code tool names. When you encounter these in a skill, use your platform equivalent:

| Skill references | Copilot CLI equivalent |
|-----------------|----------------------|
| `Read` (file reading) | `view` |
| `Write` (file creation) | `create` |
| `Edit` (file editing) | `edit` |
| `Bash` (run commands) | `bash` |
| `Grep` (search file content) | `grep` |
| `Glob` (search files by name) | `glob` |
| `Skill` tool (invoke a skill) | `skill` |
| `WebFetch` | `web_fetch` |
| `Task` tool (dispatch subagent) | `task` |
| Multiple `Task` calls (parallel) | Multiple `task` calls |
| `TodoWrite` (task tracking) | `sql` with built-in `todos` table |
| `WebSearch` | No equivalent — use `web_fetch` with a search engine URL |
| `EnterPlanMode` / `ExitPlanMode` | No equivalent — stay in the main session |

## Agent types

| Claude Code agent | Copilot CLI equivalent |
|-------------------|----------------------|
| `general-purpose` | `"general-purpose"` |
| `Explore` | `"explore"` |
| Named plugin agents (e.g. `superpowers:code-reviewer`) | Discovered automatically from installed plugins |

## Additional Copilot CLI tools

| Tool | Purpose |
|------|---------|
| `store_memory` | Persist facts about the codebase for future sessions |
| `report_intent` | Update the UI status line with current intent |
| `sql` | Query the session's SQLite database (todos, metadata) |
| `fetch_copilot_cli_documentation` | Look up Copilot CLI documentation |
| GitHub MCP tools | Native GitHub API access (issues, PRs, code search) |
