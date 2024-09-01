#!/bin/bash

if [[ $1 = "-smt" ]]; then
	pactl set-sink-mute @DEFAULT_SINK@ toggle
elif [[ $1 = "-smi" ]]; then
	pactl set-sink-volume @DEFAULT_SINK@ -5%
elif [[ $1 = "-spl" ]]; then
       	pactl set-sink-volume @DEFAULT_SINK@ +5%
elif [[ $1 = "-mmt" ]]; then
	pamixer --default-source -t
elif [[ $1 = "-bmi" ]]; then
	brightnessctl -c backlight set 5-%
elif [[ $1 = "-bpl" ]]; then
	brightnessctl -c backlight set +5%
elif [[ $1 = "-wlan" ]]; then
	sudo nmtui
elif [[ $1 = "-next" ]]; then
	playerctl next
elif [[ $1 = "-prev" ]]; then
	playerctl previous
elif [[ $1 = "-ppause" ]]; then
	playerctl play-pause
elif [[ $1 = "-h" ]]; then 
	echo "		------------------------------------------------------------------	
		Help Menu for Multimedia buttons on the ThinkPad X1 Carbon 6th Gen
		-smi and -spl lower and raise volume, -smt mutes it, -mmt the mic.
		-bmi and -bpl lower and raise the lcd brightness
		-wlan opens sudo nmtui.
		------------------------------------------------------------------
	"
else
	echo "Unknown opion, enter -h for help."
fi	
