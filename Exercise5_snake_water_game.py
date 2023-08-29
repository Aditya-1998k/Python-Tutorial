"""
Snake Water Gun games
------------------
snake, water and gun is a variation
of th echildren's game. The gun beats
the snake, snake beats the water
and water beats the gun.
Write a python program to create a snake
water gun game in python using if else statement.
do not create any fancy gui. Use proper function
to check for win
"""
import random
arr = [-1, 0, 1]
computer_response = random.choice(arr)
user_input = int(input("0 for Snake 1 for Guns -1 for Waters: "))

def Match(user, comp):
    if user>comp:
        print(f"User Won: User:{user} and Computer:{comp}")
    elif user<comp:
        print(f"Compurter Won: User:{user} and Computer:{comp}")
    else:
        print(f"Match Draws: User:{user} and Computer:{comp}")

Match(user_input, computer_response)
