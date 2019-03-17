"""
Jim Weismamn
Spring 2019
Prg 105
6.3 exception handling
"""

def main():
    count = 0
    total = 0
    record = ""
    filename = ""

    try:
        filename = "numbers.txt"
        input_file = open(filename, "r")
        record = input_file.readline()
        record = int(record.rstrip("\n"))



        while record:
            print(record)
            total += record
            count += 1
            record = input_file.readline()
            record = record.rstrip("\n")
            record = int(record)

        input_file.close()
        print("There were " + str(total) + " numbers.")
        print("The total of all numbers was: " + str(count))
        print("The average of the numbers was: " + format(total / count), ",.2f")

    except IOError:
        print("Could not find " + filename)

    except ValueError:
        print("There was non-numeric data in this file.")
        print("Processing of this file has stopped.\n", "\t", record)


main()
