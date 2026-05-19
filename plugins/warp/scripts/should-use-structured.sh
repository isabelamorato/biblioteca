#!/usr/bin/env bash
# Determines if Warp build supports structured notifications
# Returns 0 if structured notifications are supported, 1 otherwise

if [[ -n "$WARP_CLI_AGENT_PROTOCOL_VERSION" ]] && [[ -n "$WARP_CLIENT_VERSION" ]]; then
  exit 0
else
  exit 1
fi
