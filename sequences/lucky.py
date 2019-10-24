import copy
def lucky():
    sequence = []

    for each in range(0,10):
        sequence.append(each)
    active_indx = 1
    active = sequence[active_indx]
    while active_indx < len(copy.copy(sequence)):
        if sequence.index(active) % 2 == 0:
            sequence.pop(-active_indx)
        active_indx += 1
        active = sequence[-active_indx]

    print(sequence)
lucky()
