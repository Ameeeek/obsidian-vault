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


# Simulate an eavesdropper intercepting the message
def intercept_message(encrypted_message, key):
    try:
        intercepted_message = decrypt_message(encrypted_message, key)
        print("Eavesdropper intercepts and decrypts message:", intercepted_message)
    except Exception as e:
        print("Eavesdropper fails to decrypt the message:", str(e))


# Example usage
if __name__ == "__main__":
    # User A's message
    original_message = "This is a secret message"

    # User A sends an encrypted message
    encrypted_message = send_message(original_message, key)

    # Simulate an eavesdropper intercepting the message with the correct key
    intercept_message(encrypted_message, key)  # Using the correct key

    # User B receives and decrypts the message
    decrypted_message = receive_message(encrypted_message, key)
