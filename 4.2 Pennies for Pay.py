""" 
jim weisman
spring 2019
PGR105
"""
days_worked = int(input("Enter how many days did you work: "))
money = .01
pennies = 0

print("Days Worked | Amount Earned That Day")
print("------------------------------------")

for day in range(days_worked):
    money = 2 * money
    pennies += money
    print(format(day, "20,.0f") + " | $ " + format(money, "20,.2f"))

total = pennies * .01

print("\nTotal Earned over", str(days_worked), "is: $", format(pennies / 2, ',.2f'))
