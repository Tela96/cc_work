import random
import string


def excluder(orig_list):
    exc_list = []
    for item in orig_list:
        if item not in exc_list:
            exc_list.append(item)
    print (exc_list)


def letter_gen():
    letter_list = []
    for letter in range(0, 10):
        letter_list.append(random.choice(string.ascii_lowercase))
    return letter_list


def num_gen():
    num_list = []
    for i in range(0, 6):
        num_list.append(random.randint(0, 4))
    return num_list


def main():
    num_list = num_gen()
    letter_list = letter_gen()
    excluder(num_list)
    excluder(letter_list)


main()
