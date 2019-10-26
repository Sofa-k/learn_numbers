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
    global_line = res.denester(global_line,16,len(global_line)/16)
    print('----------------------------------------------------------------')
    for each in global_line:
        print(each)
    print('----------------------------------------------------------------')
