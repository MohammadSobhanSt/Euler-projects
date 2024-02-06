def factor_prime(n):

    if n <= 1:
        raise ValueError("n must be greater than 1")

    if n % 2 == 0:
        print("this is prime factor: ", 2)
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            print("this is prime factor: ", i)
            n //= i

    if n > 1:
        print("this is prime factor: ", n)


factor_prime(600851475143)
