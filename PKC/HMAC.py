import hashlib

key= input("Enter the desired key :")

secret_key = key.encode('utf-8')

hello =input("Enter the message :")

message = hello.encode('utf-8')

ipad = 0x36
opad = 0x5C


def xor_bytes(b1, b2):
    return bytes(x ^ y for x, y in zip(b1, b2))


if len(secret_key) > 64:
    secret_key = hashlib.sha256(secret_key).digest()
secret_key = secret_key.ljust(64, b'\0')
key_xor_ipad = xor_bytes(secret_key, bytes([ipad] * 64))
key_xor_opad = xor_bytes(secret_key, bytes([opad] * 64))


inner_hash = hashlib.sha256(key_xor_ipad + message).digest()
hmac = hashlib.sha256(key_xor_opad + inner_hash).digest()

print("HMAC:", hmac.hex())
