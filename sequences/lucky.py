import copy
def lucky():
    def eliminator(step,sequnce_i):
        each = 1
        while each<len(sequnce_i):
            if (each+1) % step == 0:
                sequnce_i.pop(each)
                each += 1
            each += 1

        return sequnce_i
    sequence = []
    for each in range(1,10):
        sequence.append(each)

    print(sequence)
    done = eliminator(2,sequence)
    print(done)

lucky()
