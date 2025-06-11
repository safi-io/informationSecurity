# Caesar Cipher Encryption and Decryption using Modular Arithmetic

# Function to encrypt plaintext using Caesar Cipher
def encrypt(plaintext, shift):
    encrypted_text = ""  # Store the result of encryption

    # Loop through each character in the input string
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            # Convert character to lowercase and get its position from 'a' (0 to 25)
            ascii_offset = ord('a') if char.islower() else ord('A')  # handle uppercase too
            original_position = ord(char) - ascii_offset

            # Apply Caesar Cipher formula: C = (P + shift) % 26
            new_position = (original_position + shift) % 26

            # Convert back to character and add to result
            encrypted_char = chr(new_position + ascii_offset)
            encrypted_text += encrypted_char
        else:
            # If it's not a letter (e.g., space or punctuation), leave it unchanged
            encrypted_text += char

    return encrypted_text


# Function to decrypt ciphertext using Caesar Cipher
def decrypt(ciphertext, shift):
    decrypted_text = ""  # Store the result of decryption

    # Loop through each character in the input string
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            # Get offset depending on case
            ascii_offset = ord('a') if char.islower() else ord('A')
            original_position = ord(char) - ascii_offset

            # Apply Caesar Cipher decryption: P = (C - shift) % 26
            new_position = (original_position - shift) % 26

            # Convert back to character and add to result
            decrypted_char = chr(new_position + ascii_offset)
            decrypted_text += decrypted_char
        else:
            # Leave non-alphabetic characters unchanged
            decrypted_text += char

    return decrypted_text


# Main program execution
# Ask user for plaintext input
plaintext = input("Enter the plaintext: ")

# Ask user for shift value, convert to integer
shift = int(input("Enter the shift value: "))

# Encrypt the plaintext
encrypted = encrypt(plaintext, shift)
print("Encrypted text:", encrypted)

# Decrypt the encrypted text back to original
decrypted = decrypt(encrypted, shift)
print("Decrypted text:", decrypted)
