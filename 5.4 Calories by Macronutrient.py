"""
Jim Weisman
Prg 105
Spring 2019
5.4 calories by macro nutrients
"""

def main():
    fat_total = fat_calc()
    print("You had " + str(fat_total) + " calories from fat today.")
    carb_total = carb_calc()
    print("You had " + str(carb_total) + " calories from fat today.")
    protein_total = prot_calc()
    print("You had " + str(protein_total) + " calories from fat today.")
    total = str(format(fat_total + carb_total + protein_total, ","))
    print("You had a total of " + total + " calories today.")


def fat_calc():
    fat_grams = int(input("How many grams of fat did you consume today?: "))
    return fat_grams * 9


def carb_calc():
    carb_grams = int(input("How many grams of carbs did you consume today?: "))
    return carb_grams * 4


def prot_calc():
    prot_grams = int(input("How many grams of protein did you consume today?: "))
    return prot_grams * 4


main()

