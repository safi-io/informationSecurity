from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Function to encrypt
def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Using ECB mode
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

# Function to decrypt
def des_decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    return decrypted_text.decode()

# Example usage
key = b"12345678"  # 8-byte key
plain_text = "Hello"

# Encrypt the text
encrypted_text = des_encrypt(plain_text, key)
print("Encrypted:", encrypted_text)

# Decrypt the text
decrypted_text = des_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
