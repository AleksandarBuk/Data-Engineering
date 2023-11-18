#!/bin/bash

#OPENvpn

# Variables
VPN_CONFIG="/path/to/your/vpnconfig.ovpn"
VPN_CREDENTIALS="/path/to/your/credentials.txt"
LOG_FILE="/var/log/openvpn.log"

# Check if the OpenVPN config file exists
if [ ! -f "$VPN_CONFIG" ]; then
    echo "VPN configuration file not found: $VPN_CONFIG"
    exit 1
fi

# Check if the credentials file exists
if [ ! -f "$VPN_CREDENTIALS" ]; then
    echo "VPN credentials file not found: $VPN_CREDENTIALS"
    exit 1
fi

# Starting VPN Connection
echo "Starting VPN connection..."
openvpn --config "$VPN_CONFIG" --auth-user-pass "$VPN_CREDENTIALS" --log "$LOG_FILE" &

echo "VPN connection initiated. Check $LOG_FILE for details."
