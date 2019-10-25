import copy
import random
def lucky_numbers(difficulty):

    raw = []
    lucky_raw = []
    def eliminator(raw,step):
        i = 0
        output_list = []
        while i < len(raw):
            if ((i+1) % (step) != 0):
                output_list.append(raw[i])
            i += 1
        return output_list
    for each in range(1,1500,2):
        raw.append(each)
    f = 1
    while 1:
        raw = eliminator(raw,raw[f])
        if raw == eliminator(raw,raw[f]):
            break
        f += 1
    return raw[random.randint(difficulty[0],difficulty[-1])]

def prime_numbers(numbers):
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

def ulam_numbers(difficulty):
    arr = [1,2]
    arr2 = set()
    arr2.add(1)
    arr2.add(2)
    for i in range(3, 1000):
        if len(arr) == 50:
            break
        count = 0
        for j in range(0, len(arr)):
            if (i - arr[j]) in arr2 and arr[j] != (i - arr[j]):
                count += 1
            if count > 2:
                break
        if count == 2:
            arr.append(i)
            arr2.add(i)
    return arr[random.randint(difficulty[0],difficulty[-1])]
