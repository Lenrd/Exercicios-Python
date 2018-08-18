# maior e menor na tupla
from random import randint
lista = []

for i in range(5):
    lista.append(randint(1, 10))

numeros = (lista[0], lista[1], lista[2], lista[3], lista[4])

print(f'Lista de numeros{numeros}')
maior = menor = lista[0]
for j in numeros:
    if j > maior:
        maior = j
    elif j < menor:
        menor = j
print(f'O maior numero é {maior}, O menor numero é {menor}')
