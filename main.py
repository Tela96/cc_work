from methods.sum2 import sum2
while True:
    try:
        number1 = int(input("first num: "))
        number2 = int(input("second num:"))
        number = 0
        number = sum2 (number1, number2)
        print(number)
    except ValueError :
        break