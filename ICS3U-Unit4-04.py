#!/usr/bin/env python3

# Created by: Emmanuel Fofeyin
# Created on: Oct 2022
# This program is a number guessing game
# Using break statements.

import random


def main():

    # input and variables
    random_number = random.randint(0, 9)

    # process and output
    try:
        while True:
            guessed_number_as_string = input("Enter a number between 0 and 9: ")
            guessed_number_as_number = int(guessed_number_as_string)
            if guessed_number_as_number == random_number:
                print("\nYou guessed correctly!")
                break
            elif guessed_number_as_number > random_number:
                print("\n{} is higher than the random number.".format(guessed_number_as_string))
            elif guessed_number_as_number < random_number:
                print("\n{} is lower than the random number.".format(guessed_number_as_string))
    except ValueError:
        print("\nNot good, {} is not an integer.".format(guessed_number_as_string))
    finally:
        print("\nThanks for playing.")
    print("\nDone.")


if __name__ == "__main__":
    main()
    