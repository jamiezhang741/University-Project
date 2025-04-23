# Assignment 4: Encryption Implementation
# Author: Jamie Zhang
# Date: April 8, 2025

import base64
import hashlib
from cryptography.fernet import Fernet

def generate_key():
    """Generate a key for encryption and decryption"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_message(message, key):
    """Encrypt a message using the provided key"""
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """Decrypt a message using the provided key"""
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

def main():
    # Sample usage
    message = "My research findings are getting interesting. I should document this somewhere safer than GitHub."
    
    # Generate or load key
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    except FileNotFoundError:
        key = generate_key()
    
    # Encrypt and decrypt message
    encrypted = encrypt_message(message, key)
    print(f"Encrypted message: {encrypted}")
    
    decrypted = decrypt_message(encrypted, key)
    print(f"Decrypted message: {decrypted}")
    
    # TODO: Implement more robust storage for keys
    # Maybe use the same approach as my Instagram backup solution?

if __name__ == "__main__":
    main()

# NOTES
# Although I usually dont do this but just for remebrence leaving this here "verystrongpassword" 
