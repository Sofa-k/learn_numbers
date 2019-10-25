import random
def define_prime_numbers(numbers):
    figures = []
    for i in range(numbers[1] + 1):
        figures.append(i)

    prime_numbers = []
    for number in range(len(figures)):
        if (number == 1) or (number == 2):
            prime_numbers.append(number)
        else:
            count = 2
            while count <= number:
                if count == number:
                    prime_numbers.append(number)
                    break
                if number % count == 0:
                    break
                else:
                    count += 1
                    continue

    index = random.randrange(len(prime_numbers))
    return prime_numbers[index]


print(define_prime_numbers([0, 100]))
