"""
jim weisman
spring 2019
python
"""

class Question:

    def __init__(self, question, a1, a2, a3, a4, answer):
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__answer = answer

    def set_question(self, question):
        self.__question = question

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self, a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self, a4):
        self.__a4 = a4

    def set_answer(self, answer):
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_answer(self):
        return self.__answer


def main():

    q1 = Question("A(n) ______ is a set of instructions that a computer follows to perform a task. ", "A. compiler", "B. program", "C. interpreter",
                  "D. programming language", "B")

    q2 = Question("The physical devices that a computer is made of are referred to as", "A. hardware", "B. software", "C. the operating system", "D. tools",
                  "A")

    q3 = Question("The part of a computer that runs programs is called?", "A. RAM", "B. secondary storage", "C. main memory", "D. the CPU",
                  "D")

    q4 = Question("CPUs are small chips known as ", "A. ENIACs", "B. microprocessors", "C. memory chips",
                  "D. operating systems", "B")

    q5 = Question("The computer stores a program while the program is running, as well as the data that the program is working with, in what? ", "A. secondary storage", "B. the CPU", "C. main memory", "D. the microprocessor", "C")

    q6 = Question("This is a volatile type of memory that is used only for temporary storage while a program is running. ", "A. RAM", "B. secondary storage", "C. the disk drive", "D. the USB drive", "A")

    q7 = Question("A type of memory that can hold data for long periods of time, even when there is no power to the computer, is called?", "A. RAM", "B. main memory", "C. secondary storage", "D. CPU storage", "C")

    q8 = Question("A component that collects data from people or other devices and sends it to the computer is called? ", "A. an output device", "B. an input device", "C. a secondary storage device", "D. main memory", "B")

    q9 = Question("A video display is a(n) device.", "A. output", "B. input", "C. secondary storage", "D. main memory", "B")

    q10 = Question("A ___ is enough memory to store a letter of the alphabet or a small number. ", "A. byte", "B. bit", "C. switch", "D. transistor", "B")

    player1 = 0
    player2 = 0

    set_1 = [q1, q3, q5, q7, q9]
    set_2 = [q2, q4, q6, q8, q10]

    print("Player 1: ")
    for query in set_1:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        ans = input("Please enter the letter of the correct answer: ")
        if ans.upper() == query.get_answer():
            print("You are correct!")
            player1 += 1
        else:
            print("Sorry, that was not correct.")

    print("Player 1 earned " + str(player1) + " points.")

    print("Player 2: ")
    for query in set_2:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        ans = input("Please enter the letter of the correct answer: ")
        if ans.upper() == query.get_answer():
            print("You are correct!")
            player2 += 1
        else:
            print("Sorry, that was not correct.")

    print("Player 2 earned " + str(player2) + " points.")


main()
