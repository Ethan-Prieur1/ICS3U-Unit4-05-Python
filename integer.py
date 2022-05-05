# Created by Ethan Prieur
# Created on May 2022
# This program calculates sum of positive integers


import random


def main():
    # This function uses a for loop
    counter = 0
    total = 0

    # Input
    number_as_string = input("How many number(s) are you going to add: ")

    # Process & Output
    try:
        number_as_integer = int(number_as_string)
        for counter in range(number_as_integer):
            counter = counter + 1
            second_input_str = input("Enter your number(s): ")
            print("")
            second_input_int = int(second_input_str)
            if second_input_int < 0:
                continue
            total = total + second_input_int

        print("The sum of the positive numbers is = {0}".format(total))

    except Exception:
        print("Enter integer next time pal")

    print("\nDone.")


if __name__ == "__main__":
    main()
