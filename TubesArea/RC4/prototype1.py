import os  # use for getenv
from Crypto.Cipher import ARC4  # use for cryptographic
from dotenv import load_dotenv  # load the env

load_dotenv()  # load the dotfiles
secret_key = os.getenv("SECRET_MESSAGE")
key = secret_key  # ini key nya, mungkin nanti bisa ku pindahkan ke .env
cipher = ARC4.new(secret_key)  # ini instance, Cyphernya, hanya bisa digunakan satu kali
encrypted = cipher.encrypt(b"This is a secret message")  # ini proses enkripsi

# Decryption
cipher_decrypt = ARC4.new(secret_key)  # ini instance decrypt
decrypted = cipher_decrypt.decrypt(encrypted)  # ini proses dekripsi
# print(decrypted)
