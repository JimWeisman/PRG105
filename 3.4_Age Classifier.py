#jim weisman
# PRG105
# 3.4 Age Classifier
"""
    If the person is 1 year old or less, he or she is an infant.
    If the person is older than 1 year but younger than 13 years, he or she is a child.
    If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
    If the person is at least 20 years old, he or she is an adult.
"""

age = int(input("Please enter your age:   "))

if age <= 1:
    print("you are an infant")

elif age  > 1 and age<= 13:
    print("you are an child")

elif age  >13 and age<= 20:
    print("you are an teenager")

elif age >= 20:
    print("you are an adult")


