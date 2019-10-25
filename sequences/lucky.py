import copy
def lucky():
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

    for each in range(1,20,2):
        raw.append(each)
    print(raw)
    hog = eliminator(raw,3)
    hog2 = eliminator(hog,5)
    print(hog)
    print(hog2)




print(lucky())
