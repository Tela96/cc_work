# Bad solution :


def round_sum(num1, num2, num3):

    result = num1 + num2 + num3
    return result


def round_num(num):
    num = str(num)
    for dig in num:
        lastdigit = dig
    otherdigits = num.strip(lastdigit)
    lastdigit = int(lastdigit)
    digit_details = []
    if lastdigit >= 5:
        lastdigit = 0
        digit_details.append(lastdigit)
        digit_details.append("up")
    elif lastdigit < 5:
        lastdigit = 0
        digit_details.append(lastdigit)
        digit_details.append("down")

    if digit_details[1] == "up":
        otherdigits = int(otherdigits)
        otherdigits += 1
        otherdigits = str(otherdigits)
    lastdigit = str(digit_details[0])
    otherdigits = str(otherdigits)
    num = otherdigits
    num += lastdigit
    num = int(num)
    return num


num1 = round_num(164)
num2 = round_num(1034)
num3 = round_num(126)
print(round_sum(num1, num2, num3))


# good solution is like this:
'''
num = 13
while num >= 10
    num - 10
something
something

'''
