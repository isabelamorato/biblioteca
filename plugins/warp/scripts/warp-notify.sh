#!/usr/bin/env bash
# Sends OSC 777 escape sequence for Warp terminal notifications
# Usage: warp-notify.sh <title> <body>

TITLE="${1:-Claude Code}"
BODY="${2:-}"

# Send OSC 777 notification
printf "\033]777;notify;%s;%s\007" "$TITLE" "$BODY"
