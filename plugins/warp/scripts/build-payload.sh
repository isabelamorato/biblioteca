#!/usr/bin/env bash
# Builds structured JSON payload for warp://cli-agent using jq
# Usage: build-payload.sh <title> <body>

TITLE="${1:-Claude Code}"
BODY="${2:-}"

jq -n --arg title "$TITLE" --arg body "$BODY" '{
  "title": $title,
  "body": $body
}'
