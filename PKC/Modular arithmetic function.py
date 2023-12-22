def mod_addition(a, b, modulus):
    return (a + b) % modulus

def mod_subtraction(a, b, modulus):
    return (a - b) % modulus

def mod_multiplication(a, b, modulus):
    return (a * b) % modulus

def mod_division(a, b, modulus):
    # Assuming b has a modular multiplicative inverse
    inverse_b = pow(b, -1, modulus)
    return (a * inverse_b) % modulus

# Example usage:
a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
modulus = int(input("Enter the modulus :"))

add_result = mod_addition(a, b, modulus)
sub_result = mod_subtraction(a, b, modulus)
mul_result = mod_multiplication(a, b, modulus)
div_result = mod_division(a, b, modulus)

print(f"{a} + {b} mod {modulus} = {add_result}")
print(f"{a} - {b} mod {modulus} = {sub_result}")
print(f"{a} * {b} mod {modulus} = {mul_result}")
print(f"{a} / {b} mod {modulus} = {div_result}")
