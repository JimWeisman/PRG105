"""
jim weisman
spring2018
python

"""


class Employee:
    def __init__(self, em_name, em_num):
        self.__em_name = em_name
        self.__em_num = em_num

    def set_em_name(self, em_name):
        self.__em_name = em_name

    def set_em_num(self, em_num):
        self.__em_num = em_num

    def get_em_name(self):
        return self.__em_name

    def get_em_num(self):
        return self.__em_num


class ProductionWorker(Employee):
    def __init__(self, em_name, em_num, shift_num, hourly_rate):
        Employee.__init__(self, em_name, em_num)
        self.__shift_num = shift_num
        self.__hourly_rate = hourly_rate

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def get_shift_num(self):
        return self.__shift_num

    def get_hourly_rate(self):
        return self.__hourly_rate


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
