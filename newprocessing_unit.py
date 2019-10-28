import sequences
from essential import *
from res import *

man_live = 5
user_live = 5



def input_validator(x):
    try:
        x = int(x)
        if x>0:
            return True
        else:
            print("The number can't be negative")
            return False
    except:
        print("Please enter digits, not symbols")
        return False

def choose_difficulty():
    print("choose diffilty from 1 to 3")           #    <-  Ілюстрації до складності на весь екран
    game_difficulty = input()
    if input_validator(game_difficulty)==True:
        game_difficulty = int(game_difficulty)
        if (game_difficulty>=1) and (game_difficulty<=3):
            return game_difficulty


#  Вибір рівня складності


while man_live > 0 and user_live > 0:
    #  DRAW   <- Малюється ігрове поле з револьвером і ковбоєм
    print("Question + Choose ulam number to pick the right bullet!")
    user_answer = input()
    if input_validator(user_answer)==True:
        user_answer = int(user_answer)
        if user_answer==256:
            man_live -= 1
    else:
        continue

print("While has finis")



