def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A' if char.isupper() else 'a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result


data = input("Enter the Data to Encrypt: ")
rotations = int(input("Enter the Key for Rotations: "))

cipher_data = caesar_cipher(data, rotations)
print("CIPHER TEXT:", cipher_data)
print("PLAIN TEXT:", caesar_cipher(cipher_data, -rotations))
