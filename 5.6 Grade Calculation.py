"""
Write a program that asks a user to enter five test scores.
You will need to create five variables to hold these scores.

The purpose of this assignment is to get practice passing information
between functions, this is not a good example of the way programs are really
written, but it will help you to understand how to pass parameters.
"""


def grade_avg(average):
    pass


def main(*score):
    total = 0
    score = 0

    score1 = float(input("What is your first test score?: "))
    score2 = float(input("What is your second test score?: "))
    score3 = float(input("What is your third test score?: "))
    score4 = float(input("What is your fourth test score?: "))
    score5 = float(input("What is your fifth test score?: "))

    average = calc_average(score1, score2, score3, score4, score5)
    grade_avg(average)
    print("Your average score is a " + str(average))


def calc_average(score1, score2, score3, score4, score5):
    average = int(score1 + score2 + score3 + score4 + score5) / 5
    return average


main()
