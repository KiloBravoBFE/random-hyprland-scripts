#!/bin/bash

currBrt="$(brightnessctl g)"
maxBrt="$(brightnessctl m)"
minBrt="0%"

if [[ "$currBrt" < 800 ]]; then
	brightnessctl -c backlight set "$maxBrt"
fi

if [[ "$currBrt" > 950 ]]; then
	brightnessctl -c backlight set "$minBrt"
fi
