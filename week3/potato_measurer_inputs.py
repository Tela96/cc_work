

def get_potato_price():
    taters = 0
    while taters == 0:
        try:
            taters = input("How much does a tater cost?: ")
            taters = int(taters)
        except ValueError:
            taters = 0
    return taters


def get_potato_quantity():
    taters = 0
    while taters == 0:
        try:
            taters = input("How many taters do u want to buy?: ")
            taters = int(taters)
        except ValueError:
            taters = 0
    return taters
