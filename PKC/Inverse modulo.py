def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    if a == 1:
        return x1 % m0
    else:
        return None

a = int(input("The number for which the modular inverse is to be found :"))
m = int(input("Enter the modulus :"))

inverse = mod_inverse(a, m)

if inverse is not None:
    print(f"The modular inverse of {a} modulo {m} is {inverse}.")
else:
    print(f"No modular inverse exists for {a} modulo {m}.")
