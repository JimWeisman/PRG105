"""
jim weisman
spring2018
python
redo
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
