def get_input():
    userinput = input("How big of a tree do you want? ")
    return userinput


def handle_input(userinput):

    try:
        userinput = int(userinput)
    except ValueError:
        handle_input(get_input())
    return userinput


def draw_tree(handled_input):
    for i in range(1, handled_input + 1):
        for j in range(0, i):
            print("#", end='')
        print("")


def main():
    draw_tree(handle_input(get_input()))


main()
