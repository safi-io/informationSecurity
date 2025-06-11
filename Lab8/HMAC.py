import hmac
import hashlib

# Step 1: Define a secret key for HMAC. This should be kept private.
secret_key = b'super_secret_key'  # Must be bytes, not string

# Step 2: Initialize HMAC object with the secret key and chosen hash function (e.g., SHA-256)
hmac_obj = hmac.new(secret_key, digestmod=hashlib.sha256)

# Step 3: Open the target file in binary mode for accurate reading
file_path = 'message.txt'  # The file should contain "Hello"

try:
    with open(file_path, 'rb') as file:
        # Step 4 and 5: Read the file in chunks and update HMAC with each chunk
        while True:
            chunk = file.read(1024)  # Read 1024 bytes at a time
            if not chunk:  # Stop when the end of the file is reached
                break
            hmac_obj.update(chunk)  # Update the HMAC with this chunk

    # Step 6: Finalize the HMAC computation and retrieve the digest
    hmac_digest = hmac_obj.hexdigest()  # Hexadecimal format is human-readable

    # Step 7: Output the final HMAC digest
    print("HMAC Digest (hex):", hmac_digest)

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
