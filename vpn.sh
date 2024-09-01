#!/bin/bash

if [[ $1 = "-def" ]]; then
       nmcli con down id Skara
       currCon="$(nmcli -t con | head -n 1)"
       IFS=: read -r currSSID param <<< $currCon
       #literalSSID="'"$currSSID"'"'
       #echo $currSSID
       #echo $literalSSID
       nmcli con up id Skara
       sudo nmcli con modify "$currSSID" ipv6.method 'disabled'
       #nmcli con modify 'FRITZ!Box 7490' ipv6.method 'disabled'

elif [[ $1 = "-defdn" ]]; then
       nmcli con down id Skara
       currCon="$(nmcli -t con | head -n 1)"
       IFS=: read -r currSSID param <<< $currCon
       sudo nmcli con modify "$currSSID" ipv6.method 'auto'

elif [[ $1 = "-h" ]]; then
       echo "
              You may use the following params:
              
              -def To connect to default VPN (id:Skara)
              -defdn To disconnect from default VPN (id:Skara)
       "


else
       echo "Unknown param"
fi