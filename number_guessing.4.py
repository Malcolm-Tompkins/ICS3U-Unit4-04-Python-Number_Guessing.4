#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 17, 2021
# Less complex version of the number guessing game

import random
from os import system, name
# From https://www.codespeedy.com/clear-screen-in-python/


# Function that runs Guess the number game
def main():
    # User input
    print("Welcome to Guess the number!\nPick a number from 0-9")
    # Process
    program_number = random.randint(0, 9)
    while True:

        user_input = (input("Enter your number: "))
        system('clear')
        # From https://www.codespeedy.com/clear-screen-in-python/
        try:
            user_number = int(user_input)
            if (user_number == program_number):
                system('clear')
                print("Correct!")
                print("You guessed {}".format(user_number))
                break
            else:
                print("Incorrect try again")

        except Exception:
            print("{} is not an integer".format(user_input))
    print("Done.")


if __name__ == "__main__":
    main()
