from Car import *


def main():
    car_1 = Car("Grey", "Tesla", 203942, "Gal")
    car_2 = Car("Red", "Chevrolet", 384738, "Yoav")
    car_3 = Car("Black", "Volvo", 392847, "Maya")
    car_4 = Car("White", "Tesla", 938472, "James")

    car_1.print_details()
    car_2.print_details()
    car_3.print_details()
    car_4.print_details()


main()