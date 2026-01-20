#!/usr/bin/env bash

# let's hope we don't crash :thumbsup:
set -euo pipefail

# Find active ethernet interfaces
active_conns=$(nmcli -t -f UUID,TYPE,DEVICE connection show --active \
  | awk -F: '$3 ~ /^enp/ {print $1}')

if [[ -n "$active_conns" ]]; then
  for conn in $active_conns; do
    echo "nmcli connection down \"$conn\""
    nmcli con down "$conn"
  done

# This is hard-coded for now, might change that at another point. But all my devices only have one wired connection.
else
  nmcli con up "Wired connection 1"
fi
