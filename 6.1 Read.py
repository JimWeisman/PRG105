""""
jim weisma
PRG 105
Sring 2019
chapter 6 _Practice 6.1 Read
"""

def main():
    count = 0
    names_list = open("names.txt", "r")

    record = names_list.readline()
    record = record.rstrip('\n')

    while record != "":
        print(record)
        record = names_list.readline()
        record = record.strip('\n')

    with open("names.txt", "r") as f:
        for line in f:
            print(line)
            count += 1
    print("There are " + str(count) + " names in this file.")

    names_list.close()


main()
