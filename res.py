revolver = r"""
                       X
    _   _________=__   X
    \\@([____]_____()  X
    _/\|-[____]        X
    /     /(( )        X
    /____|             X
    \____/             X
                       X
"""



def denester(asciistr,height):
    '''
    function that makes a lists from an ascii docstring image
    >>> denester([--+--X\n--+--X],2)
    [['-', '-', '+', '-', '-'], ['-', '-', '+', '-', '-']]
    '''
    output_list = []
    asciistr = list(asciistr)
    width = len(asciistr)/height
    i = 1
    ch = 0
    while i <= height:
        line = []
        while ch < width:
            if (asciistr[ch] == 'X'):
                break
            elif (asciistr[ch] != '\n'):
                line.append(asciistr[ch])
            ch += 1
        ch += 1
        i += 1
        width *=2
        output_list.append(line)
    return output_list
