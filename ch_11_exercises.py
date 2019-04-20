"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
print("=" * 10, "Section 11.1 inheritance", "=" * 10)


# You are going to create a Dwelling class based on the
# Automobile sample from the chapter


# 1) Create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors

class Dwelling:
    def __init__(self, number_of_rooms, square_feet, floors):
        self.number_of_rooms = number_of_rooms
        self.square_feet = square_feet
        self.floors = floors

    # 2) Add mutators for all of the data attributes (number_of_rooms, square_feet, floors)
    def set_number_of_rooms(self, num_room):
        self.number_of_rooms = num_room

    def set_square_feet(self, num_sq_ft):
        self.square_feet = num_sq_ft

    def set_floors(self, floorNum):
        self.floors = floorNum

    # 3) Add accessors for all of the data attributes
    def get_number_of_rooms(self):
        return self.number_of_rooms

    def get_square_feet(self):
        return self.square_feet

    def get_floors(self):
        return self.floors


print()

house = Dwelling(4, 900, 5)
print(house.floors)
print(house.get_floors())


# 4) Create the class Single_family_home as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
# -- Call the __init__ of superclass Dwelling and pass the required arguments, remember to include self
# -- Initialize the garage_type and yard_size attributes
class Single_family_home(Dwelling):

    def __init__(self, number_of_rooms, square_feet, floors, garage_type, yard_size):

        Dwelling.__init__(self, number_of_rooms, square_feet, floors)
        self.garage_type = garage_type
        self.yard_size = yard_size

    # 5) Create the mutator and accessor methods for the garage_type and yard_size attributes

    def set_garage_type(self, garage_type):
        self.garage_type = garage_type

    def get_garge_type(self):
        return self.garage_type

    def set_yard_size(self, yard_size):
        self.yard_size = yard_size

    def get_yard_size(self):
        return self.yard_size


# 6) Demonstrate the Single_family_home class, no need to import because you are in the same file
# 7) Create an object from the Single_family_home class with the following information:
# 6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres

home = Single_family_home(6, 1200, 1, 'Single Car Garage', '.25 Acres')

# 8) Display the data using the accessor methods
print('Rooms: ', home.get_number_of_rooms())
print('Square Feet: ', home.get_square_feet())
print('Floors:', home.get_garge_type())
print('Garage Type: ', home.get_garge_type())
print('Yard size: ', home.get_yard_size())

# print("# 9) Create a main function. Call the main function")
# 9) Create a main function. Call the main function


# TODO 11.2 Polymorphism
print("=" * 10, "Section 11.2 polymorphism", "=" * 10)

# 1) Type in the mammal class from program 11-9, lines 1 - 22
class Mammal:
    def __init__(self,species):
        self.__species = species
    def show_species(self):
        print(' I am a ', self.__species)
    def make_sound(self):
        print('nani?')


# 2) Create a Mouse class as a sub class of the mammal class following the Dog example

class Mouse(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Mouse')
    def make_sound(self):
        print('squeak')

# 3) Create a Bird class as a sub class of the mammal class following the Cat Example

class Bird(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Bird')
    def make_sound(self):
            print('Chirp?')


# 4) Follow the example in program 11-10 (no need to import, use main2 instead of main

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

def main2():
    mammlOBJ = Mammal('Regular Animal')
    mouseOBJ = Mouse()
    birdOBJ = Bird()

    print('here are some Animals and the sound they make!!!!')
    print()
    show_mammal_info(mammlOBJ)
    print()
    show_mammal_info(birdOBJ)
    print()
    show_mammal_info(mouseOBJ)
    print()

main2()

#    because there is already a main on this page) use the Mouse and Bird class that you created
