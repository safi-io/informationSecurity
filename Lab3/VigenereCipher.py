def encrypt(plain_data, encryption_key):
    result = ""

    i = 0
    for char in plain_data:
        plain_char_ascii = ord(char) - ord('A')
        key_char_ascii = ord(encryption_key[i % len(encryption_key)]) - ord('A')
        cipher_char_ascii = (plain_char_ascii + key_char_ascii) % 26
        cipher_char = chr(cipher_char_ascii + ord('A'))
        result += cipher_char
        i = i + 1

    return result

data = input("Enter the Data to Encrypt: ")
key = input("Enter the Encryption Key: ")

encrypted_data = encrypt(data, key)
print(encrypted_data)
