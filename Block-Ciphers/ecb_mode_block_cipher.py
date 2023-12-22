from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad_message(message):
    # Pad the message to be a multiple of 16 bytes (AES block size)
    padding_length = 16 - (len(message) % 16)
    return message + bytes([padding_length] * padding_length)

def unpad_message(padded_message):
    # Remove the padding from the message
    padding_length = padded_message[-1]
    return padded_message[:-padding_length]

def encrypt_ecb_mode(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = pad_message(plaintext)
    ciphertext = cipher.encrypt(padded_message)
    return ciphertext

def decrypt_ecb_mode(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = cipher.decrypt(ciphertext)
    return unpad_message(padded_message)

if __name__ == '__main__':
    # Generate a random 128-bit key
    key = get_random_bytes(16)

    # Example usage
    ask = input("Enter the plain text :")
    plaintext = ask.encode('utf-8')
    ciphertext = encrypt_ecb_mode(key, plaintext)
    decrypted_text = decrypt_ecb_mode(key, ciphertext)
    print(type(ciphertext))

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted text:", decrypted_text)
