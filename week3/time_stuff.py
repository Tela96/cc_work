def user_input():
    var = input("give me some times: ")
    conv_var = ""
    for char in var:
        if char != ".":
            conv_var += char

    return conv_var


def calc_diff(var1, var2):
    if int(var1) > int(var2):
        var = int(var1) - int(var2)
        return var
    else:
        var = int(var2) - int(var1)
        return var


def main():
    var1 = user_input()
    var2 = user_input()
    print(var1, var2)
    print(calc_diff(var1, var2))


main()
