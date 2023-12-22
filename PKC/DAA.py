#DAA 
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

message = b"Hello, World!"

private_key = RSA.import_key(private_key)
hash_obj = SHA256.new(message)
signature = pkcs1_15.new(private_key).sign(hash_obj)

public_key = RSA.import_key(public_key)
try:
    hash_obj = SHA256.new(message)
    pkcs1_15.new(public_key).verify(hash_obj, signature)
    print("Signature is valid.")
except (ValueError, TypeError):
    print("Signature is not valid.")