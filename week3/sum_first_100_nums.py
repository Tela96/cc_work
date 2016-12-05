def sum_var():
    sumvar = 0
    for i in range(1, 101):
        sumvar += i
    print(sumvar)


def multiply_vars():
    multvar = 1
    for i in range(1, 101):
        multvar = multvar * i
    print (multvar)


def main():
    sum_var()
    multiply_vars()

main()
