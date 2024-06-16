import os
from Crypto.Cipher import ARC4
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
secret_key = os.getenv("SECRET_MESSAGE")

# Ensure the secret key is in bytes
key = secret_key.encode()  # Convert the key to bytes


# Function to encrypt a message
def encrypt_message(message, key):
    cipher = ARC4.new(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message


# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    cipher = ARC4.new(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message


# Simulate User A sending a message
def send_message(message, key):
    encrypted_message = encrypt_message(message, key)
    print("User A sends encrypted message:", encrypted_message)
    return encrypted_message


# Simulate User B receiving a message
def receive_message(encrypted_message, key):
    decrypted_message = decrypt_message(encrypted_message, key)
    print("User B receives decrypted message:", decrypted_message)
    return decrypted_message


# Example usage
if __name__ == "__main__":
    # User A's message
    original_message = "This is a secret message"

    # User A sends an encrypted message
    encrypted_message = send_message(original_message, key)

    # User B receives and decrypts the message
    decrypted_message = receive_message(encrypted_message, key)
