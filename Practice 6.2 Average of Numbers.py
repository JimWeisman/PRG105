"""
Jim Weismamn
Spring 2019
Prg 105
6.2 Average of the Numbers
"""
def main():
    input_file = open("numbers.txt", "r")
    total = 0
    num_lines = 0
    line = input_file.readline()

    while line != "":
        num_lines += 1
        total += int(line)
        line = input_file.readline()

    average = total / num_lines

    print("There were " + str(num_lines) + " numbers")
    print("The total of all numbers was: " + format(total, ","))
    print("The average of the numbers was: " + format(average, ",.2f"))

    input_file.close()


main()
