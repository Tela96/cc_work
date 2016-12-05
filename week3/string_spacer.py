string = input("Give me a string: ")
newstring = ""
for char in string:
    if char != " ":
        newstring += char
        newstring += " "
print(newstring)
