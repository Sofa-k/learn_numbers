import copy
def lucky():
    def eliminator(step,sequnce_i):
        each = 0
        while each<len(sequnce_i):
            if each in sequnce_i:
                sequnce_i.remove(each)
            each += step
            print('hhh')
        return sequnce_i
    sequence = []
    for each in range(1,10):
        sequence.append(each)
    print(sequence)
    print(eliminator(2,sequence))
    print(eliminator(3,sequence))
lucky()
