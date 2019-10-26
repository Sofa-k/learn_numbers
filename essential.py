import sys
import res
def draw(text_area,gun,man,heart,user_live,man_live,score):
    global_line = []
    status_line = []
    score = 'Score: ' + str(score)
    #add hearts of user
    heart_u = heart[0]*user_live+heart[1]*user_live
    heart_u = denester(heart_u,2,len(heart[0])*user_live)
    #add hearts of man
    heart_m = heart[0]*man_live+heart[1]*man_live
    heart_m = denester(heart_m,2,len(heart[0])*man_live)

    # by default line lenght = 93 but it is calucalated after line 25 if this is line 14
    space1 = ' '*((93//2)-len(heart_u[0])-len(score))
    space2 = ' '*((93//2)-len(heart_m[0])-len(score))

    status_line.extend(''.join(heart_u[0]+space1+score+space2+heart_m[0]+'H'))
    status_line.extend(''.join(' '+heart_u[1]+space1+' '*len(score)+space2+' '+heart_m[1]+'H'))
    status_line = denester(status_line,2,len(status_line)/2)

    for each in status_line:
        print('\033[1;31;40m {}'.format(each))

    #code below adds two pictures of a gun and a man
    for line in range(16):
        if line < 9:
            global_line.extend(''.join(gun[line]+man[line]+'H'))

        else:
            global_line.extend(''.join(text_area[line-9]+man[line]+'H'))
    global_line = denester(global_line,16,len(global_line)/16)
    score = 123
    print('\033[1;37;40m-'*len(global_line[1]))

    for each in global_line:
        print(each)
def question_text_formator(question_text,text_area):
    text_area = list(text_area)
    i = 0
    j = 0
    while i < len(text_area):
        if (i != 0 or i != -1) and j < 4:
            print(j,'hahah')
            text_area[i+1]= '| '+ question_text[j] + ' '*(58-len(question_text[j])-1) + '|'
            print(j,'nope')
            j += 1
        i += 1
    return text_area
def denester(asciistr,height,width):
    '''
    (string,int) -> list
    function slices an ascii docstring image into string lines
    >>> denester([--+--X\n--+--X],2)
    [['-', '-', '+', '-', '-'], ['-', '-', '+', '-', '-']]
    '''
    output_list = []
    asciistr = list(asciistr)
    i = 1
    ch = 0

    while i <= height:
        line = []
        while ch < width:
            if (asciistr[ch] == 'H'):
                break
            if (asciistr[ch] == '\\'):
                pass # a bug here with slash
            if (asciistr[ch] != '\n'):
                line.append(asciistr[ch])
            ch += 1

        ch += 1
        i += 1
        width *=2
        output_list.append(''.join(line))
    return output_list
