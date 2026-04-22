"""This is a simple dice simulator program that generates a random number between 1 and 6 to mimic rolling a dice. 
The user can choose to roll the dice multiple times or exit the game. 
It demonstrates the use of loops, conditional statements, and random number generation in Python.  """

import random

print("🎲 Dice Simulator")

while True:
    roll = input("\nRoll the dice? (y/n): ").lower()

    if roll == 'y':
        dice = random.randint(1, 6)
        print("You rolled:", dice)
    elif roll == 'n':
        print("Thanks for playing! 👋")
        break
    else:
        print("⚠️ Invalid input! Please enter y or n.")
