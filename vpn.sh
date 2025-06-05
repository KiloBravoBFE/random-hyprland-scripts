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

elif [[ $1 = "-up" ]] && [[ $2 != "" ]]; then
       currCon="$(nmcli -t con | head -n 1)"
       IFS=: read -r currSSID param <<< $currCon
       if [[ "$currSSID" == "$2" ]]; then
              nmcli con down id "$2"
              currCon="$(nmcli -t con | head -n 1)"
              IFS=: read -r currSSID param <<< $currCon
              echo "++ Already connected to VPN, disconnecting."
       fi
       if [[ "$3" != "-ipv6" ]]; then
              sudo nmcli con modify "$currSSID" ipv6.method 'disabled'
			  echo "++ IPv6 protocol should now be disabled."
       fi
       nmcli connection up id "$2"
       echo "++ You should now be connected. Enter -down $2 as param to disconnect."

elif [[ $1 = "-down" ]] && [[ $2 != "" ]]; then
       nmcli con down id "$2"
       currCon="$(nmcli -t con | head -n 1)"
       IFS=: read -r currSSID param <<< $currCon
       sudo nmcli con modify "$currSSID" ipv6.method 'auto'
       nmcli connection up "$currSSID"
       echo "++ You should now be disconnected and IPv6 should be active (again)."

elif [[ $1 = "-h" ]]; then
       echo '
              You may use the following params:
              
                -up   $your-vpn-id [-ipv6]  To connect to custom VPN
                -down $your-vpn-id          To disconnect from custom VPN

                -def                        To connect to default VPN (id:Skara)
                -defdn                      To disconnect from default VPN (id:Skara)

				Replace values beginning with $ with you inputs. Do not enter brackets.

       '


else
       echo "Unknown param"
fi
