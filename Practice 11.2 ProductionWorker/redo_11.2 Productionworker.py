"""
jim weisman
spring2018
python
redo
"""

import employee



def main():
    name = input("Enter Employee Name: ")
    num = int(input("Enter Employee Number: "))
    hourly = float(input("Enter Hourly Pay Rate: "))
    shift = int(input("Enter Shift Number: "))

    if shift == 1:
        shift = 'Day'
    else:
        shift = 'Night'

    main_info = employee.Employee(name, num)
    shift_info = employee.ProductionWorker(name, num, shift, hourly)

    print("")
    print("--------------------------")
    print("Details of Employee:")
    print("--------------------------")
    print("Name:", main_info.get_em_name())
    print("Employee Number:", main_info.get_em_num())
    print("Pay Rate:", shift_info.get_hourly_rate())
    print("Shift Number:", shift_info.get_shift_num())


main()
