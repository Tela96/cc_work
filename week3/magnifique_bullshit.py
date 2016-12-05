import random

lista = [1, 2, 3, 45, 6, 7, 8, 2110, 10000]
valtozo = 0
for i in range(len(lista)):
    while valtozo != lista[i]:
        valtozo = random.randint(1, 10000)
        print(valtozo)
