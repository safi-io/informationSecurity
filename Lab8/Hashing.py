import hashlib
import os

# Function to generate a hash for a given password using a random salt
def hash_password(password):
    # Step 1: Generate a random 16-byte salt
    salt = os.urandom(16)  # 128-bit salt for good randomness

    # Step 2: Combine password (converted to bytes) with the salt
    password_bytes = password.encode('utf-8')  # Convert password string to bytes
    salted_password = password_bytes + salt    # Concatenate password bytes with salt

    # Step 3: Hash the salted password using SHA-256
    hash_object = hashlib.sha256(salted_password)
    password_hash = hash_object.digest()  # Get the binary hash output

    # Step 4: Return both the salt and the hash (for storage)
    return salt, password_hash


# Function to verify a password against stored salt and hash
def verify_password(stored_salt, stored_hash, input_password):
    # Convert input password to bytes and concatenate with stored salt
    input_bytes = input_password.encode('utf-8')
    salted_input = input_bytes + stored_salt

    # Hash the input using SHA-256
    input_hash = hashlib.sha256(salted_input).digest()

    # Compare the newly calculated hash with the stored one
    return input_hash == stored_hash


# Demonstration of how this works

# Ask user to input a password
original_password = input("Set your password: ")

# Hash the password and store the salt and hash
salt, password_hash = hash_password(original_password)

print("Password has been securely hashed and salted.")
print("Stored salt (hex):", salt.hex())
print("Stored hash (hex):", password_hash.hex())

# Ask user to verify the password
attempt = input("\nRe-enter password to verify: ")

# Check if the entered password matches the original
if verify_password(salt, password_hash, attempt):
    print("Password verification successful.")
else:
    print("Password verification failed.")
