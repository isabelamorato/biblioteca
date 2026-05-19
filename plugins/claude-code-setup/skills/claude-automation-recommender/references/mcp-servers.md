# MCP Server Recommendations

MCP (Model Context Protocol) servers extend Claude's capabilities by connecting to external tools and services.

## Setup

- **Project config** (`.mcp.json`) - Available only in that directory
- **Global config** (`~/.claude.json`) - Available across all projects
- **Checked-in `.mcp.json`** - Available to entire team (recommended!)

## Quick Reference: Detection Patterns

| Look For | Suggests MCP Server |
|----------|--------------------|
| Popular npm packages | context7 |
| React/Vue/Next.js | Playwright MCP |
| `@supabase/supabase-js` | Supabase MCP |
| `pg` or `postgres` | PostgreSQL MCP |
| GitHub remote | GitHub MCP |
| `.linear` or Linear refs | Linear MCP |
| `@aws-sdk/*` | AWS MCP |
| `@sentry/*` | Sentry MCP |
| `docker-compose.yml` | Docker MCP |
| Slack webhook URLs | Slack MCP |
| `@anthropic-ai/sdk` | context7 for Anthropic docs |
| Cloudflare Workers | Cloudflare MCP |
| Vercel deployment | Vercel MCP |
| Notion for docs | Notion MCP |
| Cross-session memory | Memory MCP |
