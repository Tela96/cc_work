def get_input():
    usr_inp = input("give me numebrs: ")
    return usr_inp


def reverse_square(usr_in):
    newnum = ""
    for digit in range(len(usr_in), 0, -1):
        digit = int(digit)
        newnum += (str(digit * digit))
    print (newnum)


def main():
    usrin = get_input()
    reverse_square(usrin)


main()
