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



def denester(heigh,code):
    '''
    function that makes a lists from an ascii docstring image
    '''
    output_list = []
    code = list(code)
    width = len(code)/heigh
    i = 1
    x = 0
    while i <= heigh:
        line = []
        while x < width:
            if (code[x] == 'X'):
                break
            elif (code[x] != '\n'):
                line.append(code[x])
            x += 1
        x += 1
        i += 1
        width *=2
        output_list.append(line)
    return output_list

denester(7,revolver)
