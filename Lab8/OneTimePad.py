import os

# Step 1: Generate a random key of the same length as the message
def generate_key(length):
    return os.urandom(length)  # Returns secure random bytes


# Step 2: User 1 encrypts the message using XOR with the key
def encrypt(message, key):
    message_bytes = message.encode('utf-8')  # Convert string to bytes
    encrypted_bytes = bytes([mb ^ kb for mb, kb in zip(message_bytes, key)])
    return encrypted_bytes


# Step 3: User 2 decrypts the message using the same key (XOR again)
def decrypt(ciphertext, key):
    decrypted_bytes = bytes([cb ^ kb for cb, kb in zip(ciphertext, key)])
    return decrypted_bytes.decode('utf-8')


# Step 4: Securely destroy the key (overwrite reference and delete)
def destroy_key(key):
    del key  # Remove reference; in real systems, use memory clearing techniques if needed


# --- Simulation ---

# User 1: Enter message
message = input("User 1 - Enter your secret message: ")

# Generate one-time pad key
key = generate_key(len(message))

# Encrypt message
encrypted = encrypt(message, key)
print("Encrypted message (hex):", encrypted.hex())

# Simulate sending encrypted message and key sharing (insecure in real life if reused)
# User 2: Decrypt the received message
decrypted = decrypt(encrypted, key)
print("User 2 - Decrypted message:", decrypted)

# Destroy the key after use
destroy_key(key)
