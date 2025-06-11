def arc4_encrypt(data, key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    keystream = []
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        rnd = S[(S[i] + S[j]) % 256]
        keystream.append(chr(ord(char) ^ rnd))

    return ''.join(keystream)

key = "SecretKey"
plaintext = "Hello, World!"

ciphertext = arc4_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted = arc4_encrypt(ciphertext, key)
print("Decrypted:", decrypted)
