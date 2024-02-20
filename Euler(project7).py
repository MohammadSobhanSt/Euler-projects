def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_nth_prime(n):
    count = 0
    number = 2
    while True:
        if is_prime(number):
            count += 1
            if count == n:
                return number
        number += 1


n = 10001
result = find_nth_prime(n)
print(f"The {n}th prime number is:", result)
