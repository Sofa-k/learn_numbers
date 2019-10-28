import sequences
from essential import *
from res import *
import time
enemy_health = 5
your_health = 5
score = 0
ulam_numbers = [1,2,3]
prime_numbers = [4,5,6]
lucky_numbers = [7,8,9]

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

'''
draw(revolver,cowboy_alive,heart,your_health,enemy_health,score)


while enemy_health > 0 and your_health > 0:
    drawq = question()
    print(drawq[0])
    user_input = int(input())
    if your_health == 1:
        print("Its either you or him! Make sure you don't miss this time")

    if ((user_input in ulam_numbers) and (drawq[1] == 1)) or \
            ((user_input in lucky_numbers) and (drawq[1] == 2)) or \
            ((user_input in prime_numbers) and (drawq[1] == 3)):

        enemy_health = enemy_health - 1
        print("Nice shot!", "Enemy health is now: ", enemy_health)
    else:
        your_health = your_health - 1
        print("Ouuch! That hurts", "Your healh is now: ", your_health)

'''
