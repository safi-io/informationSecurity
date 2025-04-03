def encrypt(plain_data, encryption_key):
    result = []
    key_length = len(encryption_key)

    for i, char in enumerate(plain_data):
        plain_char_ascii = ord(char) - ord('A')
        key_char_ascii = ord(encryption_key[i % key_length]) - ord('A')
        cipher_char_ascii = (plain_char_ascii + key_char_ascii) % 26
        result.append(chr(cipher_char_ascii + ord('A')))

    return ''.join(result)


def decrypt(cipher_data, decryption_key):
    result = []
    key_length = len(decryption_key)

    for i, char in enumerate(cipher_data):
        cipher_data_ascii = ord(char) - ord('A')
        key_char_ascii = ord(decryption_key[i % key_length]) - ord('A')
        plain_char_ascii = (cipher_data_ascii - key_char_ascii) % 26
        result.append(chr(plain_char_ascii + ord('A')))

    return ''.join(result)


data = input("Enter the Data to Encrypt: ").upper()
key = input("Enter the Encryption Key: ").upper()

if not data.isalpha() or not key.isalpha():
    print("Only alphabetic characters are allowed.")
    exit()

encrypted_data = encrypt(data, key)
print("Encrypted:", encrypted_data)

showDecrypted = input("Do you want to perform decryption (yes/no)? ").strip().lower()
if showDecrypted in ["yes", "y"]:
    print("Decrypted:", decrypt(encrypted_data, key))
