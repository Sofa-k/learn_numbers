import sys
import res
def draw(gun,man):

    '''for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")
    sdkmskdjslklj
    '''
    global_line = []
    for line in range(16):
        global_line.extend(''.join(gun[line]+(' '*30)+man[line]+'H'))
    global_line = denester(global_line,16,len(global_line)/16)
    print('---------------------------------------------------------------------------------------')
    for each in global_line:
        print(each)
    print('---------------------------------------------------------------------------------------')


def denester(asciistr,height,width):
    '''
    (string,int) -> list
    function slices an ascii docstring image into string lines
    >>> denester([--+--X\n--+--X],2)
    [['-', '-', '+', '-', '-'], ['-', '-', '+', '-', '-']]
    '''
    output_list = []
    asciistr = list(asciistr)
    width = len(asciistr)/height
    print(width)
    i = 1
    ch = 0
    while i <= height:
        line = []
        while ch < width:
            if (asciistr[ch] == 'H'):
                break
            elif (asciistr[ch] != '\n'):
                line.append(asciistr[ch])
            ch += 1
        ch += 1
        i += 1
        width *=2
        output_list.append(''.join(line))
    return output_list
