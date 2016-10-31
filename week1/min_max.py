import random

my_list = []
for i in range(0,20):
    my_list.append(random.randint(0, 50))
    #print(my_list[i])

max=0
number = 0
id = 0

for i in my_list:
    print(i)
    if(i>max):
        id = number
        max = i
    number += 1
#print("max: " + max)    
#print("\nMax: " + str(max) + "id:" + str(id))
print(my_list[id])

number = 0
min = 52
for i in my_list:
    if i<min:
        min = i
        id = number
    number += 1
print("\nMin: " + str(min) + " id: " + str(id))