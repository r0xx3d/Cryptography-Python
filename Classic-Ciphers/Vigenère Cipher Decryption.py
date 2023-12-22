def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key_length = len(key)

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)


encrypted_text=input("Enter the encrypted statement:")
key=input("Enter the key:")
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)



