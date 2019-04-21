"""
jim weisman
python
Spring 2019
"""


class OfficeFurniture:

    def __init__(self, material, length, width, height, price):
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price


class Desk(OfficeFurniture):
    def __init__(self, material, length, width, height, price, location_of_drawers, number_drawers):
        OfficeFurniture.__init__(self, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_drawers = number_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_drawers(self):
        return self.__number_drawers

    def __str__(self):
        the_desk = ("Category: " + self.get_catagory() + "\nMaterial: " + self.get_material() +
                    "\nLength: " + self.get_length() + "\nWidth: " + self.get_width() + "\nHeight: " +
                    self.get_height() + "\nDrawer Location: " + self.get_location_of_drawers() +
                    "\nNumber of Drawers: " + self.get_number_drawers())
        return the_desk


def main():
    Wood = OfficeFurniture("Wood Chair", "16in", "16in", "38in", "$100.00")
    leather = OfficeFurniture("Leather Chair", "40in", "33in", "36in", "$1,000.00")
    Desk = OfficeFurniture("Desk", "20in", "26in", "34in", "$250.00")
    barstool = OfficeFurniture("Bar Stool", "16.5", "16.5", "40.5", "$195.00")

    print("Item:", Wood.get_material())
    print("Dimensions:", Wood.get_length(), "x", Wood.get_width(), "x", Wood.get_height())
    print("Price:", Wood.get_price())
    print("------------------------------")

    print("Item:", leather.get_material())
    print("Dimensions:", leather.get_length(), "x", leather.get_width(), "x", leather.get_height())
    print("Price:", leather.get_price())
    print("------------------------------")

    print("Item:", Desk.get_material())
    print("Dimensions:", Desk.get_length(), "x", Desk.get_width(), "x", Desk.get_height())
    print("Price:", Desk.get_price())
    print("-----------------------------")

    print("Item:", barstool.get_material())
    print("Dimensions:", barstool.get_length(), "x", barstool.get_width(), "x", barstool.get_height())
    print("Price:", barstool.get_price())
    print("-----------------------------")

main()
