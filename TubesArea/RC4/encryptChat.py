import socket
import threading

import rsa

# jangan lupa di sniff pake sudo tcpdump -i lo -w output.pcap
public_key, private_key = rsa.newkeys(1024)
public_partner = None

choice = input(
    "Apakah kamu ingin membuat sebuah room (1) atau masuk ke room (2): "
)  # Pilihan untuk host atau connect
if choice == "1":
    # socket internet, TCP. Kalau mau diganti methodnya kayak UDP bisa ganti ke sockdgram dkk
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ini IPV4 Addrs ku, ini portnya
    # Sesuaikan IPnya sama localhost, beda jaringan beda IP, cek dengan command
    # ifconfig wlan0
    server.bind(("192.168.1.23", 9999))
    # server.bind(("172.20.10.4", 9999))
    server.listen()
    # saat client konek ke sebuah server, maka langsung diterima saja
    client, _ = server.accept()
    client.send(
        public_key.save_pkcs1("PEM")
    )  # Kirim public keynya dalam bentuk packet dalam format PEM
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # karena disini hanya berjalan disatu mesin, maka dapat dimasukkan ip dari
    # si host
    # Sesuaikan IPnya sama localhost, beda jaringan beda IP, cek dengan command
    # ifconfig wlan0
    client.connect(("192.168.1.23", 9999))
    # client.connect(("172.20.10.4", 9999))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(
        public_key.save_pkcs1("PEM")
    )  # terima public keynya dalam bentuk packet dalam format PEM
else:
    exit()


def kirim_pesan(c):
    while True:
        message = input("")
        # c.send(rsa.encrypt(message.encode(), public_partner))
        c.send(message.encode())
        print("You: " + message)


def terima_pesan(c):
    while True:
        # print("Partner: " + rsa.decrypt(c.recv(1024), private_key).decode())
        print("Partner: " + c.recv(1024).decode())


threading.Thread(target=kirim_pesan, args=(client,)).start()
threading.Thread(target=terima_pesan, args=(client,)).start()
