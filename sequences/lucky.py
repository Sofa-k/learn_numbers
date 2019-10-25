import copy
import random
def lucky(difficulty):
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
    for each in range(1,1000,2):
        raw.append(each)
    f = 1
    while 1:
        raw = eliminator(raw,raw[f])
        if raw == eliminator(raw,raw[f]):
            break
        f += 1
    return raw[random.randint(difficulty[0],difficulty[-1])]
