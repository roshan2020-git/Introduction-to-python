import random
'''

n = random.randint(1,50)# random integer from 1 to 50
print(n)
while True:
    Guess = int(input("Guess a number between 1 to 100 : "))
    if n == Guess:
        print("You Guessed the right ")
        break
    elif n<Guess:
        print("Guessed high ")
    else:
        print("Guessed low")

print("Congratulation !!! YOU finally won ")
'''
'''
print("You are now Entered in Guessing the Number Game ")
win_num = random.randint(1,100)
print(win_num)
game_over = False
guess = 1
while not game_over:
    n = int(input("Guess a number between 1 to 100 "))
    if n == win_num:
        game_over = True
        print(f"You guess the number in {guess} times")
    else:
        if n < win_num:
            print(f"Guessed very low ")
            guess += 1
        else:
            print("Guessed too high ")
            guess += 1
'''
# DRY principle of coding is Don't repeat yourself
