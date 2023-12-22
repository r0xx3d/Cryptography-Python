def vigenere_encrypt(plain_text, key):
    encrypted_text = []
    key_length = len(key)

    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)


plain_text =input("Enter the plain text:")
key = input("Enter the key:")
encrypted_text = vigenere_encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)

