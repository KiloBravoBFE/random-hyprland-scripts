#!/usr/bin/env bash

iface=$(iw dev | awk '$1=="Interface"{print $2; exit}')

if ! iw dev "$iface" link | grep -q "Connected"; then
    echo '{"text":"⚠ Err: WLAN-Kabel","tooltip":"Disconnected"}'
    exit 0
fi

info=$(iw dev "$iface" link)

ssid=$(iwgetid -r)

freq=$(awk '/freq:/ {printf "%.1f", $2/1000}' <<< "$info")

signal=$(awk '/signal:/ {print int(100-(-$2))}' <<< "$info")

if echo "$info" | grep -q "EHT"; then
    std="WiFi 7"
elif echo "$info" | grep -q "HE"; then
    std="WiFi 6"
elif echo "$info" | grep -q "VHT"; then
    std="WiFi 5"
elif echo "$info" | grep -q "HT"; then
    std="WiFi 4"
else
    std="Legacy"
fi

text="   $ssid ($std / ${freq}GHz / ${signal}%)"

tooltip=$(ip addr show "$iface" | awk '/inet /{print $2}')

printf '{"text":"%s","tooltip":"%s"}\n' "$text" "$tooltip"
