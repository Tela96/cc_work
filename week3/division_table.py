def get_input():
    try:
        userinput = input("Give the number: ")
        userinput = int(userinput)
    except ValueError:
        userinput = 1
    return userinput


def make_table():
    userinput = get_input()
    num = 1
    while num <= 10:
        print(userinput, " times ", num, " equals ", userinput * num)
        num += 1


def main():
    make_table()

main()
