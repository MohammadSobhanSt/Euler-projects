def smallest():
    number = 1
    while True:
        divisible = True
        for i in range(1, 20):
            if number % i != 0:
                divisible = False
                break
        if divisible:
            print(number)
            break
        number += 1

smallest()
