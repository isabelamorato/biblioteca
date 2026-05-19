#!/usr/bin/env bash
# Hook: Notification (idle_prompt)
# Called when Claude Code sends an idle notification

MESSAGE="${CLAUDE_NOTIFICATION_MESSAGE:-Waiting for input}"

if bash "$(dirname "$0")/should-use-structured.sh"; then
  PAYLOAD=$(bash "$(dirname "$0")/build-payload.sh" "Claude Code" "$MESSAGE")
  echo "$PAYLOAD" | warp://cli-agent
else
  bash "$(dirname "$0")/warp-notify.sh" "Claude Code" "$MESSAGE"
fi
