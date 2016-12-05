def string_somethingizer(string):
    flag = False
    newstring = ""
    for char in string:
        if char == ">":
            flag = False
        if flag:
            newstring += char
        if char == "<":
            flag = True

    print(newstring)


string_somethingizer("öljetek < meg > <pls>")
