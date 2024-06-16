
#!/bin/bash

# Nama antarmuka nirkabel
WIRELESS_INTERFACE="wlan0"

# Nama SSID (nama jaringan)
SSID="OMARKHAREEN"

# Kata sandi untuk jaringan
PASSWORD="12345omar"

# Hentikan jaringan nirkabel jika sedang berjalan
echo "Menghentikan antarmuka nirkabel..."
sudo ifconfig $WIRELESS_INTERFACE down

# Konfigurasi antarmuka nirkabel untuk WPA3
echo "Mengkonfigurasi antarmuka nirkabel untuk WPA3..."
sudo iw dev $WIRELESS_INTERFACE set type managed
sudo iw dev $WIRELESS_INTERFACE set channel 11
sudo iw dev $WIRELESS_INTERFACE set power_save off
sudo iw dev $WIRELESS_INTERFACE set txpower fixed 20dBm
sudo iw dev $WIRELESS_INTERFACE set security wpa3-psk
sudo iw dev $WIRELESS_INTERFACE set wpa_passphrase $SSID $PASSWORD

# Nyalakan kembali antarmuka nirkabel
echo "Menyalakan antarmuka nirkabel..."
sudo ifconfig $WIRELESS_INTERFACE up

# Tunggu sebentar agar antarmuka nirkabel siap
sleep 2

# Tampilkan informasi jaringan yang terhubung
echo "Jaringan nirkabel telah dikonfigurasi:"
sudo iw $WIRELESS_INTERFACE info

# Tampilkan IP Address yang diberikan oleh router
echo "IP Address yang diberikan oleh router:"
sudo dhclient -v $WIRELESS_INTERFACE &>/dev/null &

# Tangkap paket dengan tcpdump, mengecualikan paket DNS
echo "Memulai sniffing paket (kecuali DNS)..."
sudo tcpdump -i $WIRELESS_INTERFACE -w sniffed_traffic.pcap not port 53

