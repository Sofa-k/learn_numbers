import random
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
