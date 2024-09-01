#!/bin/bash

if [[ $1 = "-def" ]]; then
       currCon="$(nmcli -t con | head -n 1)"
       IFS=: read -r currSSID param <<< $currCon
       if [[ "$currSSID" == "Skara" ]]; then
              nmcli con down id Skara
              currCon="$(nmcli -t con | head -n 1)"
              IFS=: read -r currSSID param <<< $currCon
              echo "++ Already connected to VPN, disconnecting."
       fi
       sudo nmcli con modify "$currSSID" ipv6.method 'disabled'
       nmcli connection up "$currSSID"
       nmcli con up id Skara
       echo "++ You should now be connected and IPv6 should be disabled."

elif [[ $1 = "-defdn" ]]; then
       nmcli con down id Skara
       currCon="$(nmcli -t con | head -n 1)"
       IFS=: read -r currSSID param <<< $currCon
       sudo nmcli con modify "$currSSID" ipv6.method 'auto'
       nmcli connection up "$currSSID"
       echo "++ You should now be disconnected and IPv6 should be active again."

elif [[ $1 = "-h" ]]; then
       echo "
              You may use the following params:
              
              -def To connect to default VPN (id:Skara)
              -defdn To disconnect from default VPN (id:Skara)
       "


else
       echo "Unknown param"
fi