"""
jim weisman
spring 2019
python PRG105
"""

def Name():
    name = input("Please enter your name in the format, First Middle Last: ")
    initials = name.split()

    first = initials[0][0]
    middle = initials[1][0]
    last = initials[2][0]

    print(first.upper() + ". " + middle.upper() + ". " + last.upper() + ".")

Name()
