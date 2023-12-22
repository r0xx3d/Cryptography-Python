# caeser cipher used for encrypting messages
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char

    return result


# Usage
plaintext = input("Enter the message:")
shift = int(input("Enter the shift :"))
encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted:", encrypted_text)
