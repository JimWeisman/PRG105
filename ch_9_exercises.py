"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 9.1 Dictionaries
print("=" * 10, "Section 9.1 dictionaries", "=" * 10)
print("# 1) Finish creating the following dictionary by adding three more people and birthdays")
# 1) Finish creating the following dictionary by adding three more people and birthdays
birthdays = {'Meri': 'May 16', 'Kathy': 'July 14', 'Dave' : 'March 13' , 'Murica' : 'July'}

print("#2) Print Meri's Birthday" )

print(birthdays['Meri'])
print(birthdays)

for x in birthdays:
    print(x)

print("#3) Create an empty dictionary named registration")

registration = {}
registration['day'] = 'Monday'

print(registration)

# You will use the following dictionary for many of the remaining exercises"
miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}


print("#1) Print the keys and the values of miles_ridden using a for loop")

for x,y in miles_ridden.items():
    print(x, ' ', y)

print("# 2) Get the value for June 3 and print it, if not found display 'Entry not found', replace the """)

value = ""
try:
    value = miles_ridden ['June 3']
except:
    value = 'Value not found'
print(value)

print("3) Get the value for June 6 and print it, if not found display 'Entry not found' replace the """)
# 3) Get the value for June 6 and print it, if not found display 'Entry not found' replace the ""
value2 = ""
try:
    value2 = miles_ridden ['June 6']
except:
    value2 = 'Value not found'
print(value2)

print ("# 4) Use the items method to print the miles_ridden dictionary")

print(miles_ridden.items())

print("# 5) Use the keys method to print all of the keys in miles_ridden")
# 5) Use the keys method to print all of the keys in miles_ridden
print(miles_ridden.keys())

print("# 6) Use the pop method to remove June 4 then print the contents of the dictionary")
# 6) Use the pop method to remove June 4 then print the contents of the dictionary

print(miles_ridden.pop('June 4'))

print("# 7) Use the values method to print the contents of the miles_ridden dictionary")
# 7) Use the values method to print the contents of the miles_ridden dictionary


# TODO 9.2 Sets
print("=" * 10, "Section 9.2 sets", "=" * 10)

print("# 1) Create an empty set named my_set")
# 1) Create an empty set named my_set
my_set = {}

print("# 2) Create a set named days that contains the days of the week")
# 2) Create a set named days that contains the days of the week

days = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"}

print("# 3) Get the number of elements from the days set and print it")
# 3) Get the number of elements from the days set and print it

elements = len(days)
print(elements)

print("# 4) Remove Saturday and Sunday from the days set")
# 4) Remove Saturday and Sunday from the days set
days.add ("Holiday")
print(days)
days.remove("Saturday")
days.remove("Sunday")
print(days)


print("# 5) Determine if 'Mon' is in the days set")
# 5) Determine if 'Mon' is in the days set

if 'Mon' in days:
    print("Mon is present")
else:
    print("No Mon")

# TODO 9.3 Serializing Objects (Pickling)
print("=" * 10, "Section 9.3 serializing objects using the pickle library", "=" * 10)

print("# 1) Import the pickle library at the top of this file")
# 1) Import the pickle library at the top of this file
import pickle

print("# 2) Create the output file log and open it for binary writing")
# 2) Create the output file log and open it for binary writing

picklefile = open("Output.txt", 'wb')


print("# 3) Pickle the miles_ridden dictionary and output it to the log file")
# 3) Pickle the miles_ridden dictionary and output it to the log file

pickle.dump (miles_ridden, picklefile)

print("# 4) Close the log file")
# 4) Close the log file

picklefile.close()

birthdaysImport = {}

picklefile = open("Output.txt", 'rb')
birthdaysImport = pickle.load(picklefile)
#pickle.load(picklefile, birthdaysImport)
print(birthdaysImport)
