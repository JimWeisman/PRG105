"""
Jim weisman
Spring 2019
PRG 105
"""

import random


def main():
    random_numbers = generate_random()
    user_num = get_info()
    display(random_numbers, user_num)  # Display, not print.


def get_info():
    user_number = -1  # helps validate the catch
    while 100 < user_number or 0 > user_number:  # forces the program to keep asking for a number
        user_number = float(input("Please enter a number between 1 and 100: "))
        if user_number >= 100 or user_number < 0:  # How to check to validate a correct number
            print("That number is not in the valid range.")
    return user_number


def generate_random():
    random_integers = []
    for num in range(1, 20):
        my_random = random.randint(0, 100)  # To import the random numbers
        random_integers.append(my_random)
    return random_integers


def display(num_list, input_num):
    found = False  # How to check/validate
    for number in num_list:
        if number > input_num:
            found = True
            print(number)
    if not found:
        print("There were no matches found.")


main()

