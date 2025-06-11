from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Function to encrypt plaintext using DES and 8-bit key (padded to 8 bytes)
def encrypt_des(plaintext, key_byte):
    key = bytes([key_byte] * 8)  # Simulate 8-byte key from single byte
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return encrypted

# Function to decrypt ciphertext with a given key
def decrypt_des(ciphertext, key_byte):
    key = bytes([key_byte] * 8)  # Simulate full DES key
    cipher = DES.new(key, DES.MODE_ECB)
    try:
        decrypted_padded = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted_padded, DES.block_size)
        return decrypted.decode()
    except:
        return None  # Return None if unpadding or decoding fails (wrong key)

# Ask user for input
plaintext = input("Enter the plaintext message: ")
key_input = int(input("Enter an 8-bit key (0-255): "))

# Encrypt with the chosen key
ciphertext = encrypt_des(plaintext, key_input)
print("Encrypted (hex):", ciphertext.hex())

# Brute-force attack: try all 256 possible keys
print("\nStarting brute-force attack...")

for brute_key in range(256):
    decrypted_text = decrypt_des(ciphertext, brute_key)
    if decrypted_text == plaintext:
        print("\n Key found!")
        print("Key (decimal):", brute_key)
        print("Decrypted message:", decrypted_text)
        break
else:
    print(" Failed to decrypt. Key not found in keyspace.")
