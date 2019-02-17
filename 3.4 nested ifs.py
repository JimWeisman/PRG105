#jim weisman
# Spring 2019
# RPG 105
# project 3.4 nested ifs

package_selected = input("Which package did you purchase?: ")
minutes_used = 0

if package_selected == "A" or package_selected == "a" \
        or package_selected == "B" or package_selected == "b" \
        or package_selected == "C" or package_selected == "c":
    minutes_used = int(input("How many minutes did you use this month?: "))

if package_selected == 'A' or package_selected == 'a':
    package_cost = 39.99
    if minutes_used > 450:
        price = package_cost + ((minutes_used - 450) * .45)
        print("You owe $" + format(price, ",.2f"))
    if minutes_used < 450:
        print (" you owe nothnig extra you used less then your monthly allowance")
elif package_selected == 'B' or package_selected == 'b':
    package_cost = 59.99
    if minutes_used > 900:
        price = package_cost + ((minutes_used - 900) * .40)
        print("You owe $" + format(price, ",.2f"))
    if minutes_used < 900:
        print (" you owe nothnig extra you used less then your monthly allowance")

elif package_selected == 'C' or package_selected == 'c':
    print("You have unlimited minutes and owe nothing. Have a nice day ")




