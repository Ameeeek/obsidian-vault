import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, ARC4
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
secret_key = os.getenv("SECRET_MESSAGE").encode()  # Convert the key to bytes

# Generate RSA keys for User A and User B
user_a_key = RSA.generate(2048)
user_a_public_key = user_a_key.publickey()
user_b_key = RSA.generate(2048)
user_b_public_key = user_b_key.publickey()


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


# Simulate User A sending a message
def send_message(message, user_a_private_key, user_b_public_key, sym_key):
    # Encrypt the symmetric key with User B's public key
    rsa_cipher = PKCS1_OAEP.new(user_b_public_key)
    encrypted_sym_key = rsa_cipher.encrypt(sym_key)

    # Encrypt the message with the symmetric key
    encrypted_message = encrypt_message(message, sym_key)

    # Sign the message
    signature = sign_message(message, user_a_private_key)

    print("User A sends encrypted message and signature")
    return encrypted_sym_key, encrypted_message, signature


# Simulate User B receiving a message
def receive_message(
    encrypted_sym_key,
    encrypted_message,
    signature,
    user_b_private_key,
    user_a_public_key,
):
    # Decrypt the symmetric key with User B's private key
    rsa_cipher = PKCS1_OAEP.new(user_b_private_key)
    sym_key = rsa_cipher.decrypt(encrypted_sym_key)

    # Decrypt the message with the symmetric key
    decrypted_message = decrypt_message(encrypted_message, sym_key)

    # Verify the message
    if verify_message(decrypted_message, signature, user_a_public_key):
        print("User B verifies and decrypts the message:", decrypted_message)
    else:
        print("User B fails to verify the message")


# Example usage
if __name__ == "__main__":
    original_message = "This is a secret message"

    # User A sends an encrypted message and signature
    encrypted_sym_key, encrypted_message, signature = send_message(
        original_message, user_a_key, user_b_public_key, secret_key
    )

    # Simulate an eavesdropper intercepting the message (they can't decrypt it without the private key)
    # eavesdropper cannot do anything here as they don't have the private keys

    # User B receives and decrypts the message
    receive_message(
        encrypted_sym_key, encrypted_message, signature, user_b_key, user_a_public_key
    )
