import random
import sequences

enemy_health = 5
your_health = 5
score = 0
ulam_numbers = [1,2,3]
prime_numbers = [4,5,6]
lucky_numbers = [7,8,9]

def question():

    ulam_question = """
    +------------------------------------------------------+
    |                                                      |
    |      Choose an ULAM number                           |
    |                                                      |
    +------------------------------------------------------+
    """
    lucky_question = """
    +------------------------------------------------------+
    |                                                      |
    |      Choose an LUCKY number                          |
    |                                                      |
    +------------------------------------------------------+
    """
    prime_question = """
    +------------------------------------------------------+
    |                                                      |
    |      Choose a PRIME number                           |
    |                                                      |
    +------------------------------------------------------+
    """
    question_list = [(ulam_question,1),(lucky_question,2),(prime_question,3)]
    return random.choice(question_list)
while enemy_health > 0 and your_health > 0:
    if your_health == 1:
        print("Its either you or him! Make sure you don't miss this time")    #  <---- Пистолет направляется на юзера
    drawq = question()
    print(drawq[0])
    x = int(input())
    if ((x in ulam_numbers) and (drawq[1] == 1)) or\
       ((x in lucky_numbers) and (drawq[1] == 2)) or\
       ((x in prime_numbers) and (drawq[1] == 3)):

        enemy_health = enemy_health - 1
        print("Nice shot!","Enemy health is now: ",enemy_health)
    else:
        your_health = your_health - 1
        print("Ouuch! That hurts","Your healh is now: ",your_health)


