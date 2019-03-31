"""
jim weisman
spring2019
python prg 105
"""

def main():
    digits = ["0", "1", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6",
              "7", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "9", "-"]

    alpha = ["0", "1", "2", "A", "B", "C", "3", "D", "E", "F", "4", "G", "H", "I", "5", "J", "K", "L", "6", "M", "N",
             "O", "7", "P", "Q", "R", "S", "8", "T", "U", "V", "9", "W", "X", "Y", "Z", "-"]

    phone_num = input("Please enter the phone number 1-555-GET-FOOD or another number that you want to convert to numbers: ")

    translated_phone = ""


    for num in phone_num:
        for item in range(0, len(alpha)):
            if num.isalpha():
                num = num.upper()
            if num == alpha[item]:
                translated_phone = translated_phone + digits[item]

    print(translated_phone)


main()
