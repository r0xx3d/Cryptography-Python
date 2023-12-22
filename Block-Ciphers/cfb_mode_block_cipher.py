from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_cfb_mode(key, plaintext):
    # Generate a random IV (Initialization Vector)
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return iv + ciphertext

def decrypt_cfb_mode(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    return decrypted_data

if __name__ == '__main__':
    # Generate a random 128-bit key
    key = get_random_bytes(16)

    # Example usage
    ask = input("Enter the plain text :")
    plaintext = ask.encode('utf-8')
    ciphertext = encrypt_cfb_mode(key, plaintext)
    decrypted_text = decrypt_cfb_mode(key, ciphertext)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted text:", decrypted_text)