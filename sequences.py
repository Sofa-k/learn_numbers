import copy
import random

def sequence_cut(input_list, difficulty):
    '''
    (list,list) -> list
    function that removes all the elements that are not within the inputed range
    >>> sequence_cut([1,2,5,6,19,20,21,34,45],[6,34])
    [6, 19, 20, 21, 34]
    '''
    for each in copy.copy(input_list):
        if each < difficulty[0]:
            input_list.remove(each)
        if each > difficulty[-1]:
            input_list.remove(each)
    return input_list

def lucky_numbers(difficulty):
    '''
    (int) - > list
    
    function chooses lucky numbers from the range depending on difficulty and returns them.
    
    >>> lucky_numbers(1)
    [1, 7, 10, 13, 19]
    >>> lucky_numbers(2)
    [23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
    >>> lucky_numbers(3)
    [103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193]
    '''
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
    for each in range(1,difficulty[-1],2):
        raw.append(each)
    f = 1
    while 1:
        raw = eliminator(raw,raw[f])
        if raw == eliminator(raw,raw[f]):
            break
        f += 1
    raw = sequence_cut(raw,difficulty)
    return raw[random.randrange(len(raw))]

def prime_numbers(difficulty): 
    '''
    (int) - > list
    
    function chooses prime numbers from the range depending on difficulty and returns them.
    
    >>> prime_numbers(1)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> prime_numbers(2)
    [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    >>> prime_numbers(3)
    [103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    '''
    figures = []
    for i in range(difficulty[1] + 1):
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
    prime_numbers = sequence_cut(prime_numbers,difficulty)
    return prime_numbers[random.randrange(len(prime_numbers))]

def ulam_numbers(difficulty):
    '''
    (int) - > list
    
    function chooses Ulam numbers from the range depending on difficulty and returns them.
    
    >>> ulam_numbers(1)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> ulam_numbers(2)
    [26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99]
    >>> ulam_numbers(3)
    [102, 106, 114, 126, 131, 138, 145, 148, 155, 175, 177, 180, 182, 189, 197]
    '''
    arr = [1,2]
    arr2 = set()
    arr2.add(1)
    arr2.add(2)
    for i in range(3, difficulty[-1]):
        if len(arr) == difficulty[-1]:
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
    arr = sequence_cut(arr,difficulty)
    return arr[random.randrange(len(arr))]
