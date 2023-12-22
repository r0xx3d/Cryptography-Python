def add_points(p1, p2, a, p):
    x1, y1 = p1
    x2, y2 = p2

    if p1 == (0, 0):
        return p2
    if p2 == (0, 0):
        return p1

    if p1 != p2:
        m = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    else:
        m = ((3 * x1**2 + a) * pow(2 * y1, -1, p)) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

def multiply_point(k, p, a, b, p_value):
    result = (0, 0)
    for i in range(k.bit_length()):
        if k & (1 << i):
            result = add_points(result, p, a, p_value)
        p = add_points(p, p, a, p_value)
    return result

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


a = get_input("Enter the value of 'a' for the curve: ")
b = get_input("Enter the value of 'b' for the curve: ")
p = get_input("Enter the value of 'p' for the curve: ")


x_g = get_input("Enter the x-coordinate of the base point 'G': ")
y_g = get_input("Enter the y-coordinate of the base point 'G': ")
G = (x_g, y_g)


d = get_input("Enter the private key 'd': ")


Q = multiply_point(d, G, a, b, p)

print(f"Base Point (G): {G}")
print(f"Private Key (d): {d}")
print(f"Public Key (Q): {Q}")
