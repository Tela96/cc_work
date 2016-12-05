import random


def cow_bull():
    cow = 0
    bull = 0
    number = random.randint(1000, 9999)
    number = str(number)
    print(number)
    while True:
        guess = input("Your guess: ")
        for index in range(len(number)):
            if number[index] == guess[index]:
                cow += 1
            if number[index] in guess and number[index] != guess[index]:
                bull += 1
                print(bull)
        # print("Cow: %s\nBull: %s" % (cow, bull))
        print("Cow: ", cow, "Bull: ", bull, sep='\n')
        if cow == 4:
            print("GG m80, u wined boy")
            break
        cow = 0
        bull = 0


cow_bull()
