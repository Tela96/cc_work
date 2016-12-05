def get_input():
    var = input("Give me some shit right here: ")
    var = int(var)
    return var


def paint_shit(width, height):
    count = 1
    while count <= height:
        print("X" * width)
        count += 1


def main():
    width = get_input()
    height = get_input()
    paint_shit(width, height)


main()
