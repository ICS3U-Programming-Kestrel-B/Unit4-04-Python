#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Nov. 8, 2022
# This program asks for a guess
# from 0-9 and tells the user if
# their number is the same as the
# computer-generated answer

import math
import random


def main():
    # introductory paragraph
    print("This program asks for a guess")
    print("from 0-9 and tells the user if")
    print("their number is the same as the")
    print("computer-generated answer")
    print("")

    # input
    # generating correct_num
    import random
    correct_num = random.randint(0, 9)

    # starting while loop
    while True:
        # getting user_num_string
        user_num_string = input("Enter a number (0-9): ")
            # process
        # checking that user_num_string is an integer
        try:
            user_num_int = int(user_num_string)

            if user_num_int >= 0 and user_num_int <= 9:
                # If they guessed correctly
                if user_num_int == correct_num:
                    print("You guessed correctly!");
                    break
            else:
                print("Please enter a positive, whole integer.")
        except ValueError:
            print("Please enter a valid integer.")
        finally:
            print("Thanks for playing!")


if __name__ == "__main__":
    main()
