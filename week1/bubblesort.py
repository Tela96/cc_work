import random
import time
lista = []
for i in range(0,12):
    lista.append(random.randint(0,100))
print(lista)
for i in range (len(lista)) :
    for j in range (len(lista)) :
        if lista[j]>lista[i]:
            lista[i], lista[j] = lista[j], lista[i]
#time.sleep(2)
print(lista)


#Imi verzio:

#def bubblesort(lst):
    #nums=lst

    #for i in range(len(nums)-1,0, -1):
        #for j in range (i):
            #temp = nums[j]
            #nums[j] = nums[j+1]
            #nums[j+1] = temp
    #print(nums)



#bubblesort([9,4,5,2,3])