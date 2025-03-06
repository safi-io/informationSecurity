key = 'abcdefghijklmnopqrstuvwxyz'

def encryption(shifts, plain_text):
    result = ''
    for char in plain_text.lower():
        try:
            cipher = key[(key.index(char) + shifts) % 26]
            result += cipher
        except ValueError:
            result += char
    return result.upper()


def decryption(shifts, cipher_text):
    result = ''
    for char in cipher_text.lower():
        try:
            plain = key[(key.index(char) - shifts) % 26]
            result += plain
        except ValueError:
            result += char
    return result.upper()


data = input("Enter the Data: ")
rotations = int(input("Enter the Key: "))

cipher_data = encryption(rotations, data)
print("CIPHER TEXT:", cipher_data)
print("PLAIN TEXT:", decryption(rotations, cipher_data))