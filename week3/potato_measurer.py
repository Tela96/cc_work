
from potato_measurer_inputs import *


def tater_calc(quantity, price):
    final_price = quantity * price
    if final_price > 0:
        print("You have to pay", final_price)
    else:
        print("Wrong input")


def main():
    tater_calc(get_potato_quantity(), get_potato_price())


main()
