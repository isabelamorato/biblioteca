#!/usr/bin/env bash
# Hook: PermissionRequest
# Called when Claude Code requests permission for an action

ACTION="${CLAUDE_PERMISSION_ACTION:-unknown action}"

if bash "$(dirname "$0")/should-use-structured.sh"; then
  PAYLOAD=$(bash "$(dirname "$0")/build-payload.sh" "Claude Code - Permission Needed" "Requesting permission: $ACTION")
  echo "$PAYLOAD" | warp://cli-agent
else
  bash "$(dirname "$0")/warp-notify.sh" "Claude Code - Permission Needed" "Requesting permission: $ACTION"
fi
