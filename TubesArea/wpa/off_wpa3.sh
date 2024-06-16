#!/bin/bash

# Nama antarmuka nirkabel
WIRELESS_INTERFACE="wlan0"

# Menghentikan antarmuka nirkabel jika sedang berjalan
echo "Menghentikan antarmuka nirkabel..."
sudo ifconfig $WIRELESS_INTERFACE down

# Mengembalikan antarmuka nirkabel ke setelan awal
echo "Mengembalikan antarmuka nirkabel ke setelan awal..."
sudo iw dev $WIRELESS_INTERFACE set type managed
sudo iw dev $WIRELESS_INTERFACE set channel auto
sudo iw dev $WIRELESS_INTERFACE set power_save on
sudo iw dev $WIRELESS_INTERFACE set txpower auto
sudo iw dev $WIRELESS_INTERFACE set security open

# Menyalakan kembali antarmuka nirkabel
echo "Menyalakan antarmuka nirkabel..."
sudo ifconfig $WIRELESS_INTERFACE up

