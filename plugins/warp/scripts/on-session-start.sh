#!/usr/bin/env bash
# Hook: SessionStart
# Called when a new Claude Code session starts

if bash "$(dirname "$0")/should-use-structured.sh"; then
  PAYLOAD=$(bash "$(dirname "$0")/build-payload.sh" "Claude Code" "Session started")
  echo "$PAYLOAD" | warp://cli-agent
else
  bash "$(dirname "$0")/warp-notify.sh" "Claude Code" "Session started"
fi
