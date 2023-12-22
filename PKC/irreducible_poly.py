from sympy import Symbol, Poly, factor

# Define a symbolic variable
x = Symbol('x')


# Example: x^3 + x + 1
polynomial = Poly(x**3 + x + 1, x, domain='GF(2)')  # 'GF(2)' represents the field of two elements (0 and 1)


is_irreducible = polynomial.is_irreducible

if is_irreducible:
    print(f"The polynomial {polynomial} is irreducible over GF(2).")
else:
    factors = factor(polynomial, domain='GF(2)')
    print(f"The polynomial {polynomial} is reducible and factors as {factors}.")
