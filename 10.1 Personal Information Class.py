"""
jim weisman
spring2019
python
"""

class Human: # me and the wife
    def __init__(self, human, name, address, age, phone):
        self.__human = human
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_human(self, human):
        self.__human = human

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_human(self):
        return self.__human

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

class Dog: #the dogs
    def __init__(self, dog, name, address, age, phone):
        self._dog = dog
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_dog(self, dog):
        self._dog = set_dog

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_dog(self):
        return self._dog

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

def main():
    jim = Human("jim", "Human","1118 Leah Drive", "61", "847-639-6279")
    mary = Human("Mary", "Human", "1118 Leah Drive", "58", "847-639-6279")
    sam = Dog("Sam", "Dog", "1118 Leah Drive", "1 1/2", "847-639-6279")
    annie = Dog("Annie", "Dog", "1118 Leah Drive", "6", "847-639-6279")

    print("--------------------")
    print(jim.get_human())
    print(jim.get_name())
    print(jim.get_address())
    print(jim.get_age())
    print(jim.get_phone())

    print("--------------------")
    print(mary.get_human())
    print(mary.get_name())
    print(mary.get_address())
    print(mary.get_age())
    print(mary.get_phone())

    print("--------------------")
    print(sam.get_dog())
    print(sam.get_name())
    print(sam.get_address())
    print(sam.get_age())
    print(sam.get_phone())

    print("--------------------")
    print(annie.get_dog())
    print(annie.get_name())
    print(annie.get_address())
    print(annie.get_age())
    print(annie.get_phone())


main()

