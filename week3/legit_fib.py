def get_input():
    var = input("how many fib numbers do u want? ")
    return var


def handle_input(input):
    try:
        input = int(input)
    except ValueError:
        return 0
    return input


def fibo(input):
    limit = input
    counter = 0
    number1 = 1
    number2 = 0
    fib = 0
    fiblist = []
    while counter < limit:
        counter = counter + 1
        fib = number1 + number2
        number1 = number2
        number2 = fib
        print(fib)
        fiblist.append(fib)
    return fiblist


def fib_sum(fiblist):

    fibsum = sum(fiblist)
    print(fibsum)


def main():
    var = 0
    while var == 0:
        var = get_input()
        var1 = handle_input(var)
    fib_sum(fibo(var1))


main()
