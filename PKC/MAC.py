#MAC

import hmac
import hashlib
secret_key = b'SecretKey123'

# Message to be authenticated
message = b'Hello, World!'

# Create a MAC using HMAC and SHA-256
mac = hmac.new(secret_key, message, hashlib.sha256)

# Get the MAC digest
mac_digest = mac.digest()

verification_mac = hmac.new(secret_key, message, hashlib.sha256)
if hmac.compare_digest(mac_digest, verification_mac.digest()):
    print("MAC is valid.")
else:
    print("MAC is not valid.")