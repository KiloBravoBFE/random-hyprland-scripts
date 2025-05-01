curl -sS https://ipinfo.io/$(curl -sS https://ipinfo.io/ip) | grep -oP '"postal":\s*"\K[0-9]+'
