while True:
    try:
        num1 = int(input("Enter THE number: "))
        result = num1%3
        res2 = num1%5
        if result == 0 and res2 == 0:
            print("fizzbuzz")
        elif result == 0:
            print("fizz")
        elif res2 == 0:
            print("buzz")    

    except ValueError:
        break