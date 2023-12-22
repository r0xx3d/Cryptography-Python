a=input("Enter the statement:")
k=int(input("Enter the key:"))
def main():
    print("Rail Fence Cipher")

    print()

    clearText = a

    print("Original Text: " + clearText)

    print()

    key = k

    cipherText = cipher(clearText, key)

    print("Ciphered Text: {0}".format(cipherText))

    decipherText = decipher(cipherText, key)

    print("Deciphered Text: {0}".format(decipherText))

    return


def cipher(clearText, key):
    result = ""

    matrix = [["" for x in range(len(clearText))] for y in range(key)]

    increment = 1

    row = 0

    col = 0

    for c in clearText:

        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1

        matrix[row][col] = c

        row += increment

        col += 1

    for list in matrix:
        result += "".join(list)

    return result


def decipher(cipherText, key):
    result = ""

    matrix = [["" for x in range(len(cipherText))] for y in range(key)]

    idx = 0

    increment = 1

    for selectedRow in range(0, len(matrix)):

        row = 0

        for col in range(0, len(matrix[row])):

            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1

            if row == selectedRow:
                matrix[row][col] += cipherText[idx]

                idx += 1

            row += increment

    matrix = transpose(matrix)

    for list in matrix:
        result += "".join(list)

    return result


def transpose(m):
    result = [[0 for y in range(len(m))] for x in range(len(m[0]))]

    for i in range(len(m)):

        for j in range(len(m[0])):
            result[j][i] = m[i][j]

    return result


# main()

b=int(input("What do you want to do \n1.Encrypt\n2.Decrypt\n?? :"))
if b == 1 :
    clearText=a
    key = k
    cipherText = cipher(clearText, key)
    print("Ciphered Text: {0}".format(cipherText))
if b==2:
    clearText=a
    key=k
    input=a
    decipherText = decipher(input, key)
    print("Deciphered Text: {0}".format(decipherText))
else:
    print("xxx----xxxx----xx---x")
