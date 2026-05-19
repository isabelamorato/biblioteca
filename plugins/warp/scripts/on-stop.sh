#!/usr/bin/env bash
# Hook: Stop
# Called when a Claude Code session stops

if bash "$(dirname "$0")/should-use-structured.sh"; then
  PAYLOAD=$(bash "$(dirname "$0")/build-payload.sh" "Claude Code" "Session ended")
  echo "$PAYLOAD" | warp://cli-agent
else
  bash "$(dirname "$0")/warp-notify.sh" "Claude Code" "Session ended"
fi
