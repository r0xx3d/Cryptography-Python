from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_cbc_mode(key, plaintext):
    # Generate a random IV (Initialization Vector)
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return iv + ciphertext

def decrypt_cbc_mode(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data

if __name__ == '__main__':
    # Generate a random 128-bit key
    key = get_random_bytes(16)

    # Example usage
    ask = input("Enter the plain text :")
    plaintext = ask.encode('utf-8')
    ciphertext = encrypt_cbc_mode(key, plaintext)
    decrypted_text = decrypt_cbc_mode(key, ciphertext)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted text:", decrypted_text)
