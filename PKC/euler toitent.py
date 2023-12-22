def euler_totient(n):
    result = n

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i

    if n > 1:
        result -= result // n

    return result


num = int(input("Enter a number: "))
print(f"Euler's Totient function value for {num} is {euler_totient(num)}")
