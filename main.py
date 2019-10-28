import sequences
from essential import *
from res import *
import time

x=2
diff_list = ((0,20),(21,100),(101,200))
revolver = denester(revolver,9,len(revolver)/9)
qustion_text_1 = denester(question_text_1,5,len(question_text_1)/5)
revolver_shot = denester(revolver_shot,9,len(revolver_shot)/9)
cowboy_alive = denester(cowboy_alive,16,len(cowboy_alive)/16)
cowboy_dead = denester(cowboy_dead,16,len(cowboy_dead)/16)
user_live = denester(user_live,9,len(user_live)/9)
heart = denester(heart,2,len(heart)/2)
text_area = qustion_area_maker(qustion_text_1)


#print(sequences.lucky_numbers(diff_list[x]))
#print(sequences.prime_numbers(diff_list[x]))
#print(sequences.ulam_numbers(diff_list[x]))

#! Animation
user_x_anim = [user_x_anim_1,user_x_anim_2,user_x_anim_3,user_x_anim_4,user_x_anim_5,user_x_anim_6,user_x_anim_7,user_x_anim_1,user_x_anim_1,user_x_anim_1]
man_x_anim = [man_x_anim_1,man_x_anim_1,man_x_anim_1,man_x_anim_1,man_x_anim_1,man_x_anim_1,man_x_anim_1,man_x_anim_8,man_x_anim_9,man_x_anim_10]

anim_global_line = []
i=0
while i < len(user_x_anim):
    user_x_anim[i] = denester(user_x_anim[i],9,len(user_x_anim[i])/9)
    i+=1
i=0
while i < len(user_x_anim):
    man_x_anim[i] = denester(man_x_anim[i],16,len(man_x_anim[i])/16)
    i+=1
i=0
while i < 10:

    anim_global_line.append(draw_proccessing(text_area,user_x_anim[i],man_x_anim[i],0,0,0,0,True))

    i += 1

line = draw_proccessing(text_area,user_live,cowboy_alive,heart,5,5,134)
draw(line[0],line[1])
x = 0
while x < 10:
    draw(line[0],anim_global_line[x])
    time.sleep(0.04)
    x += 1

