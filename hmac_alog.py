import hmac
import hashlib

key = b"MySecret123"                # Convert to bytes
message = b"Hello Bob"              # Convert to bytes

mac = hmac.new(key, message, hashlib.sha256)
mac_code = mac.hexdigest()

print("MAC =", mac_code)
