import secrets

def key_generation(length):
    key = ""
    for _ in range(length):
        key += secrets.choice("01")
    return key

def xor_operation(bin1, bin2):
    result = ""
    for i in range(len(bin1)):
        result += str(int(bin1[i]) ^ int(bin2[i]))
    return result

def encrypt(key, message):
    return xor_operation(key, message)

def decrypt(key, ciphertext):
    return xor_operation(key, ciphertext)

length = 10
message = key_generation(length)
key = key_generation(length)

ciphertext = encrypt(key, message)
decrypted_message = decrypt(key, ciphertext)

print("Message:      ", message)
print("Key:          ", key)
print("Ciphertext:   ", ciphertext)
print("Decrypted Msg:", decrypted_message)
