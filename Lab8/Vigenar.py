def key_vigenere(key):
    keyArray = []
    for i in range(0, len(key)):  # ✅ Added closing parenthesis and colon
        keyElement = ord(key[i].upper()) - 65  # ✅ Added () after .upper, replaced wrong dash with minus
        keyArray.append(keyElement)  # ✅ Corrected spelling from keyElemnt to keyElement
    return keyArray

secretKey = 'DECLARATION'
key = key_vigenere(secretKey)
print(key)  # ✅ Corrected variable name from 'keys' to 'key'
