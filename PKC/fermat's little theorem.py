import random

def mod_exp(a, b, m):
    if b == 0:
        return 1
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

def is_prime_fermat(p, num_tests):
    if p <= 1:
        return False

    for _ in range(num_tests):
        a = random.randint(2, p - 1) 
        if mod_exp(a, p - 1, p) != 1:
            return False  

    return True

def main():
    num = int(input("Enter a positive integer : "))
    num_tests = int(input("Enter the number of tests : "))

    if is_prime_fermat(num, num_tests):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is composite.")

if __name__ == "__main__":
    main()