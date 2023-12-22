from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes


def pad_message(message):
    # Pad the message to be a multiple of 8 bytes (DES block size)
    padding_length = 8 - (len(message) % 8)
    return message + bytes([padding_length] * padding_length)


def unpad_message(padded_message):
    # Remove the padding from the message
    padding_length = padded_message[-1]
    return padded_message[:-padding_length]


def encrypt_3des(key, plaintext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_message = pad_message(plaintext)
    ciphertext = cipher.encrypt(padded_message)
    return ciphertext


def decrypt_3des(key, ciphertext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_message = cipher.decrypt(ciphertext)
    return unpad_message(padded_message)


if __name__ == '__main__':
    # Generate a random 192-bit (3-key) key
    key = get_random_bytes(24)

    # Example usage
    ask = input("Enter the plain text :")
    plaintext = ask.encode('utf-8')
    ciphertext = encrypt_3des(key, plaintext)
    decrypted_text = decrypt_3des(key, ciphertext)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted text:", decrypted_text)
