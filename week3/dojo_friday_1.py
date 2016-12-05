import random


def sum_while(num_list):
    total = 0
    counter = 0
    while total != sum(num_list):
        total += num_list[counter]
        counter += 1
    return total


def sum_while_2(num_list):
    total = 0
    while len(num_list) != 0:
        total += num_list[0]
        del num_list[0]
    return total

num_list = [random.randint(0, 500), random.randint(
    0, 500), random.randint(0, 500), random.randint(0, 500)]


print(sum_while(num_list))
print(sum_while_2(num_list))
s = "Halal"
s = s.strip(s[0])
print(s)
faszom = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(faszom) - 1, -1, -1):
    print (faszom[i])
string = "anna"
pal = ""
for i in range(len(string) - 1, -1, -1):
        pal += string[i]
print(pal)
