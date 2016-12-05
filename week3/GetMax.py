import random


def get_max(numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def main():
    list_o_numberz = []

    for i in range(0, 2):
        list_o_numberz.append(random.randint(0, 15))
    print(get_max(list_o_numberz))


main()
