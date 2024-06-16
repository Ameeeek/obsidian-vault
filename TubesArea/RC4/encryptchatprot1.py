import socket
import threading
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, ARC4
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from dotenv import load_dotenv

# jangan lupa di sniff pake sudo tcpdump -i lo -w output.pcap
# Load environment variables
load_dotenv()
secret_key = os.getenv("SECRET_MESSAGE").encode()  # Convert the key to bytes

# Generate RSA keys for both users
user_key = RSA.generate(2048)
public_key = user_key.publickey()
partner_public_key = None


# Function to encrypt the message with ARC4
def encrypt_message(message, key):
    cipher = ARC4.new(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message


# Function to decrypt the message with ARC4
def decrypt_message(encrypted_message, key):
    cipher = ARC4.new(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message


# Function to sign the message
def sign_message(message, private_key):
    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(h)
    return signature


# Function to verify the message
def verify_message(message, signature, public_key):
    h = SHA256.new(message.encode())
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False


choice = input(
    "Apakah kamu ingin membuat sebuah room (1) atau masuk ke room (2): "
)  # Pilihan untuk host atau connect
if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Sesuaikan IPnya sama localhost, beda jaringan beda IP, cek dengan command
    # ifconfig wlan0
    server.bind(("192.168.1.23", 9999))
    # server.bind(("172.20.10.4", 9999))

    server.listen()
    client, _ = server.accept()
    client.send(public_key.export_key())
    partner_public_key = RSA.import_key(client.recv(2048))

    # Encrypt the symmetric key with partner's public key
    rsa_cipher = PKCS1_OAEP.new(partner_public_key)
    encrypted_sym_key = rsa_cipher.encrypt(secret_key)
    client.send(encrypted_sym_key)
elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Sesuaikan IPnya sama localhost, beda jaringan beda IP, cek dengan command
    # ifconfig wlan0
    client.connect(("192.168.1.23", 9999))
    # client.connect(("172.20.10.4", 9999))
    partner_public_key = RSA.import_key(client.recv(2048))
    client.send(public_key.export_key())

    # Decrypt the symmetric key with our private key
    encrypted_sym_key = client.recv(256)
    rsa_cipher = PKCS1_OAEP.new(user_key)
    secret_key = rsa_cipher.decrypt(encrypted_sym_key)
else:
    exit()


def kirim_pesan(c):
    while True:
        message = input("")
        encrypted_message = encrypt_message(message, secret_key)
        signature = sign_message(message, user_key)
        c.send(encrypted_message + b"||" + signature)
        print("You: " + message)


def terima_pesan(c):
    while True:
        data = c.recv(1024)
        encrypted_message, signature = data.split(b"||")
        message = decrypt_message(encrypted_message, secret_key)
        if verify_message(message, signature, partner_public_key):
            print("Partner: " + message)
        else:
            print("Failed to verify the message")


threading.Thread(target=kirim_pesan, args=(client,)).start()
threading.Thread(target=terima_pesan, args=(client,)).start()
