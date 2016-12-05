stringlist = {}
string = "egy kettő kfasédf 3 négy"


def checkio(string):
    stringlist = list(string.split())
    count = 0
    for i in range(len(stringlist)):
        variable = stringlist[i]
        if variable.isdigit():
            count = 0
        else:
            count += 1
        if count == 3:
            return True
    return False


print(checkio(string))
