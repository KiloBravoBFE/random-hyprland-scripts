#!/usr/bin/env bash

json() {
    local text="$1"
    local tooltip="$2"
    local class="$3"

    text=${text//\\/\\\\}
    text=${text//\"/\\\"}

    tooltip=${tooltip//\\/\\\\}
    tooltip=${tooltip//\"/\\\"}
    tooltip=${tooltip//$'\n'/\\n}

    class=${class//\\/\\\\}
    class=${class//\"/\\\"}

    if [[ -n "$class" ]]; then
        printf '{"text":"%s","tooltip":"%s","class":"%s"}\n' "$text" "$tooltip" "$class"
    else
        printf '{"text":"%s","tooltip":"%s"}\n' "$text" "$tooltip"
    fi
}

get_ip() {
    ip -4 addr show "$1" |
        awk '/inet / {print $2}' |
        cut -d/ -f1 |
        head -n1
}

get_active_connection_name() {
    local iface="$1"

    nmcli -t -f NAME,DEVICE connection show --active |
        awk -F: -v dev="$iface" '$2==dev {print $1; exit}'
}

# VPN
vpn_info=$(
    nmcli -t --escape no -f NAME,TYPE,DEVICE connection show --active |
    awk -F: '$2=="vpn" || $2=="wireguard" {
        print $1 "|" $2 "|" $3
        exit
    }'
)

if [[ -n "$vpn_info" ]]; then
    IFS="|" read -r vpn_name vpn_type vpn_iface <<< "$vpn_info"

    vpn_ip=$(
        ip -4 addr show "$vpn_iface" 2>/dev/null |
        awk '/inet / {print $2}' |
        cut -d/ -f1 |
        head -n1
    )

    json "  $vpn_name" \
"Connection: $vpn_name
Type: $vpn_type
Interface: $vpn_iface
IP: $vpn_ip" \
"vpn"

    exit 0
fi

# Ethernet
eth_iface=$(
    nmcli -t -f DEVICE,TYPE,STATE device status |
    awk -F: '$2=="ethernet" && $3=="connected" {
        print $1
        exit
    }'
)

if [[ -n "$eth_iface" ]]; then
    eth_conn=$(
        nmcli -g GENERAL.CONNECTION device show "$eth_iface" 2>/dev/null |
        head -n1
    )

    eth_ip=$(
        ip -4 addr show "$eth_iface" 2>/dev/null |
        awk '/inet / {print $2}' |
        cut -d/ -f1 |
        head -n1
    )

    eth_speed_raw=$(cat "/sys/class/net/$eth_iface/speed" 2>/dev/null)

    case "$eth_speed_raw" in
        10) eth_speed="10 Mbit/s" ;;
        100) eth_speed="100 Mbit/s" ;;
        1000) eth_speed="1 Gbit/s" ;;
        *) eth_speed="unknown" ;;
    esac

    eth_duplex=$(cat "/sys/class/net/$eth_iface/duplex" 2>/dev/null)

    if [[ "$eth_speed" == "unknown" ]]; then
        eth_text="󰈀  Ethernet"
    else
        eth_text="󰈀  Ethernet ($eth_speed)"
    fi

    json "$eth_text" \
"Connection: ${eth_conn:-unknown}
Interface: $eth_iface
IP: ${eth_ip:-unknown}
Speed: $eth_speed
Duplex: ${eth_duplex:-unknown}" \
"ethernet"

    exit 0
fi

# WiFi
wifi_iface=$(
    nmcli -t -f DEVICE,TYPE,STATE device status |
    awk -F: '$2=="wifi" && $3=="connected" {
        print $1
        exit
    }'
)

if [[ -n "$wifi_iface" ]]; then
    info=$(iw dev "$wifi_iface" link 2>/dev/null)

    ssid=$(
        nmcli -t -f ACTIVE,SSID dev wifi |
        awk -F: '$1=="yes" {print $2; exit}'
    )

    if [[ -z "$ssid" ]]; then
        ssid=$(iwgetid "$wifi_iface" -r)
    fi

    freq=$(
        awk '/freq:/ {printf "%.1f", $2/1000}' <<< "$info"
    )

    signal_dbm=$(
        awk '/signal:/ {print int($2)}' <<< "$info"
    )

    wifi_bitrate=$(
        awk -F': ' '/tx bitrate:/ {print $2; exit}' <<< "$info"
    )

    wifi_security=$(
        nmcli -t -f ACTIVE,SECURITY dev wifi |
        awk -F: '$1=="yes" {print $2; exit}'
    )

    wifi_gateway=$(
        nmcli -g IP4.GATEWAY device show "$wifi_iface" 2>/dev/null |
        head -n1
    )

    wifi_dns=$(
        nmcli -g IP4.DNS device show "$wifi_iface" 2>/dev/null |
        awk '{printf "%s%s", (NR>1 ? ", " : ""), $0}'
    )

    if [[ -n "$signal_dbm" ]]; then
        if (( signal_dbm >= -50 )); then
            signal=100
        elif (( signal_dbm <= -100 )); then
            signal=0
        else
            signal=$(( 2 * (signal_dbm + 100) ))
        fi
    else
        signal=$(
            nmcli -t -f ACTIVE,SIGNAL dev wifi |
            awk -F: '$1=="yes" {print $2; exit}'
        )
    fi

    if echo "$info" | grep -q "EHT"; then
        std="WiFi 7"
    elif echo "$info" | grep -q "HE"; then
        if awk '/freq:/ {exit !($2 >= 5925)}' <<< "$info"; then
            std="WiFi 6E"
        else
            std="WiFi 6"
        fi
    elif echo "$info" | grep -q "VHT"; then
        std="WiFi 5"
    elif echo "$info" | grep -q "HT"; then
        std="WiFi 4"
    else
        std="WiFi"
    fi

    wifi_ip=$(get_ip "$wifi_iface")
    wifi_conn=$(get_active_connection_name "$wifi_iface")

    json "   $ssid ($std / ${freq}GHz / ${signal}%)" \
"Connection: $wifi_conn
Interface: $wifi_iface
IP: $wifi_ip
Bitrate: ${wifi_bitrate:-unknown}
Security: ${wifi_security:-unknown}
Gateway: ${wifi_gateway:-unknown}
DNS: ${wifi_dns:-unknown}" \
"wifi"

    exit 0
fi

# LTE / mobile broadband
lte_iface=$(
    nmcli -t -f DEVICE,TYPE,STATE device status |
    awk -F: '$2=="gsm" && $3=="connected" {
        print $1
        exit
    }'
)

if [[ -z "$lte_iface" ]]; then
    lte_iface=$(
        nmcli -t -f DEVICE,TYPE,STATE device status |
        awk -F: '$2=="cdma" && $3=="connected" {
            print $1
            exit
        }'
    )
fi

if [[ -n "$lte_iface" ]]; then
    lte_ip=$(get_ip "$lte_iface")
    lte_conn=$(get_active_connection_name "$lte_iface")

    json "󰖩 LTE" \
"Connection: $lte_conn
Interface: $lte_iface
IP: $lte_ip"

    exit 0
fi

# Fallback
json "⚠ Err: WLAN-Kabel" "Disconnected" "disconnected"