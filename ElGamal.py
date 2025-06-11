import random
from sympy import mod_inverse, isprime

# Step 1: Key Generation
def generate_keys(p):
    assert isprime(p), "p must be a prime number"

    g = random.randint(2, p - 2)  # generator
    x = random.randint(2, p - 2)  # private key
    y = pow(g, x, p)              # public key: y = g^x mod p

    public_key = (p, g, y)
    private_key = x
    return public_key, private_key

# Step 2: ElGamal Encryption
def elgamal_encrypt(m, public_key):
    p, g, y = public_key
    k = random.randint(2, p - 2)  # random ephemeral key
    c1 = pow(g, k, p)
    s = pow(y, k, p)              # shared secret
    c2 = (m * s) % p
    return (c1, c2)

# Step 3: ElGamal Decryption
def elgamal_decrypt(ciphertext, private_key, p):
    c1, c2 = ciphertext
    s = pow(c1, private_key, p)
    s_inv = mod_inverse(s, p)
    m = (c2 * s_inv) % p
    return m

# Step 4: Simulate the CCA (Chosen Ciphertext Attack)
def simulate_cca(ciphertext, alpha, public_key, decryption_oracle):
    c1, c2 = ciphertext
    p, g, y = public_key

    # Attacker modifies ciphertext to predictably alter plaintext
    modified_c2 = (c2 * alpha) % p
    modified_ciphertext = (c1, modified_c2)

    # Oracle decrypts modified ciphertext
    decrypted_modified_message = decryption_oracle(modified_ciphertext)
    print(f"[Attacker] Modified Ciphertext Decrypted (should be alpha * m): {decrypted_modified_message}")

    # Recover original message using knowledge of alpha
    recovered_message = (decrypted_modified_message * mod_inverse(alpha, p)) % p
    print(f"[Attacker] Recovered Original Message: {recovered_message}")
    return recovered_message

# ========== Main Simulation ==========
def main():
    # Simulate ElGamal with a small prime for demonstration
    p = 467  # In practice, use large primes (2048+ bits)
    public_key, private_key = generate_keys(p)
    print("[System] Public Key:", public_key)
    print("[System] Private Key:", private_key)

    # Message to encrypt
    message = 123
    ciphertext = elgamal_encrypt(message, public_key)
    print(f"[System] Original Ciphertext: {ciphertext}")

    # Define the decryption oracle accessible to attacker
    def decryption_oracle(cipher):
        return elgamal_decrypt(cipher, private_key, public_key[0])

    # Attacker chooses multiplier alpha
    alpha = 2
    print(f"[Attacker] Chosen alpha: {alpha}")

    # Perform the attack
    simulate_cca(ciphertext, alpha, public_key, decryption_oracle)

if __name__ == "__main__":
    main()
