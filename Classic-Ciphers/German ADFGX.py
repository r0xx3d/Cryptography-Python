import string

# Define the ADFGX square
adfgx_square = [
    'A', 'D', 'F', 'G', 'X',
    'D', 'G', 'A', 'X', 'F',
    'G', 'X', 'D', 'F', 'A',
    'X', 'A', 'G', 'F', 'D',
    'F', 'F', 'X', 'G', 'X',
]

def create_key_square(key):
    key = ''.join(sorted(key))
    key_square = []

    for letter in key:
        if letter not in key_square:
            key_square.append(letter)

    for letter in string.ascii_uppercase:
        if letter not in key_square:
            key_square.append(letter)

    return key_square

def adfgx_encrypt(message, key):
    key_square = create_key_square(key)
    message = message.upper().replace("J", "I")

    cipher_text = ""

    for char in message:
        if char in string.ascii_uppercase:
            index = key_square.index(char)
            row = index // 5
            col = index % 5
            cipher_text += adfgx_square[row] + adfgx_square[col]

    return cipher_text

def adfgx_decrypt(cipher_text, key):
    key_square = create_key_square(key)

    plain_text = ""
    index = 0

    while index < len(cipher_text):
        row = adfgx_square.index(cipher_text[index])
        col = adfgx_square.index(cipher_text[index + 1])
        index += 2
        letter_index = row * 5 + col
        plain_text += key_square[letter_index]

    return plain_text

# Example usage
key = "SECRET"
message = "HELLO"
cipher_text = adfgx_encrypt(message, key)
print("Cipher text:", cipher_text)

decrypted_text = adfgx_decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)




