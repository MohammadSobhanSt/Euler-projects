def even_fibonacci_sum(a, b, n):
    total_even_sum = 0
    while a < n:
        if a % 2 == 0:
            total_even_sum += a
        a, b = b, a + b
    return total_even_sum


first_number = int(input("enter your first number: "))
second_number = int(input("enter your second number: "))
max_term = 4000000

result = even_fibonacci_sum(first_number, second_number, max_term)
print(result)

