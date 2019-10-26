revolver = r"""
                       H
                       H
                       H
                       H
    _   _________=__   H
    \\@([____]_____()  H
    _/\|-[____]        H
    /     /(( )        H
    /____|             H
    \____/             H
                       H
                       H
                       H
                       H
                       H
                       HHeight16
"""
revolver_shot = r"""
                                        H
                           _ ' '        H
    _   _________=__   ''     '  '      H
    \\@([____]_____()-----BBBBD     ' ' H
    _/\|-[____]         ''  '  '        H
    /     /(( )              '    '     H
    /____|                              H
    \____/                              H
                                        H
                                        H
                                        H
                                        H
                                        H
                                        H
                                        HHeight16
"""
cowboy_alive = """
             ___              H
          __|___|__           H
           ('o_o')            H
.___ __    _\~-~/_            H
' ---[_)~ / /\__/\\           H
     (_\/. )O  O(  \          H
       \_/ \    /  /          H
          /_|  |_\(           H
         / /(\/)\ \\          H
        /_/      \_\          H
       (_||      ||_)         H
         \| |__| |/           H
          | |  | |            H
          | |  | |            H
          |_|  |_|            H
          /_\  /_\            HHeight16
"""
cowboy_dead = """
             ___              H
          __|___|__           H
           ('X_X')            H
.___ __    _\~-~/_            H
' ---[_)~ / /\__/\\           H
     (_\/. )O  O(  \          H
       \_/ \    /  /          H
          /_|  |_\(           H
         / /(\/)\ \\          H
        /_/      \_\          H
       (_||      ||_)         H
         \| |__| |/           H
          | |  | |            H
          | |  | |            H
          |_|  |_|            H
          /_\  /_\            HHeight16
"""
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

revolver = denester(revolver,16,len(revolver)/16)
cowboy_alive = denester(cowboy_alive,16,len(cowboy_alive)/16)
revolver_shot = denester(revolver_shot,8,len(revolver_shot)/8)
