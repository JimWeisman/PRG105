
# jim weisman spring 2019 python PRG-105






def main():
    alpha = ["A", "a","B", "b","C","c", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
             "T", "U", "V", "W", "X", "Y", "Z", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
             "t", "u", "v", "w", "x", "y", "z"]

    user_string = input("Enter a phrase: ")
    common_letters = ""
    maximum = 0
    count = 0

    for char in alpha:
        for letter in user_string:
            if char == letter.upper():
                count += 1

        if count > maximum:
            maximum = count
            common_letters = char
            count = 0
        elif count == maximum:
            common_letters = common_letters + " " + char
            count = 0
        else:
            count = 0

    print("The most common letter is ")
    print(common_letters + " appeared " + str(maximum) + " times.")


main()
