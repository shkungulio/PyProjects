#!/bin/env python3

import random # Import random module of the python

"""
Guessing Game: Created using Python
#1 Allows user to enter lower and upper boundaries
#2 The computer will randomly generate a number to be guessed.
#3 The user will try to guess the number.
"""
def guess(x, y):
    random_number = random.randint(x, y) # Generate a random number to be guessed
    guess = 0
    while guess != random_number:
        guess = int(input(f'I am thinking of a number between {x} and {y}, Can you guess it?: '))
        if guess < random_number: # Check if the guessed number is lower than the generated guess
            print('Sorry that number is too low, GUESS AGAIN')
        elif guess > random_number: # Check if the guessed number is higher than the generated guess
            print('Sorry that number is too hight, GUESS AGAIN')
    print(f'Congratulation!!! the guess between {x} and {y} is {guess}')

def check():
    print() # Print empty line for readability purposes
    print("Help me to create boundarie of the Game!")
    print('-----------------------------------------')
    try: 
        low = int(input("Please enter the lower boundary: ")) # Prompts user to enter lower boundary
        high = int(input("Please enter the upper boundary: ")) # Prompt user to enter upper boundary
        guess(low, high) # Calling guess function while passing low and high as parameters
    except Exception:
        print('Something wrong with your input! TRY AGAIN') # Print this line if user enters others than integer
check()