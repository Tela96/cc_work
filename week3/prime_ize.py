import random


def primal_decider(number):
    number = int(number)
    for i in range(2, number - 1):
        if number % i == 0:
            return "number is not prime"
            else:
            return "number is prime"


def main():
    number = input("give me some shit right'ere: ")
    print(primal_decider(number))


main()
