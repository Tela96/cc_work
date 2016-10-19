
while True:
    try:
        n1 = int(input('Type in the first number : '))
        op = input('Define the operation : ')
        n2 = int(input('Type in the second number : '))
        if op == "+":
            print(n1, op, n2, '=', n1+n2)
        elif op == "-":
            print(n1, op, n2, '=', n1-n2)
        elif op == "*":
            print(n1, op, n2, '=', n1*n2)
        elif op == "/":
            print(n1, op, n2, '=', n1/n2)
        else:
            print('Please use valid operators!')
            break    

    except ValueError:
        print('We are working with numbers, not letters! Quitting...')
        break

