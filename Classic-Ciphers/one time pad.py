import random

def generate_key(length):
    return [random.randint(0, 25) for _ in range(length)]

def encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - offset + key[i]) % 26 + offset)
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    return encrypt(ciphertext, [-k for k in key])  # Decryption is essentially encryption with the negated key

# Example usage:
plaintext = input("Enter plain text :")
key = generate_key(len(plaintext))

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(ciphertext, key)


proce=input("Enter 'Yes' if you want to decrypt the message else 'No' :")
a=proce.lower()
if a=="yes":
    print("Decrypted Text:", decrypted_text)
else:
    print(f"^_^--x--^_^--x--^_^--x--^_^--x--^_^\nThe key is {key}")


