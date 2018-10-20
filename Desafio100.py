# sorteio e soma de pares

from random import randint
from time import sleep

def sorteio():
    lista = []
    for i in range(5):
        num = randint(1, 100)
        lista.append(num)
    print('Sorteando numeros da lista:', end=' ')

    for numero in lista:
        print(numero, end=' ')
        sleep(0.5)
    print('PRONTO!')
    return lista

def soma_pares(lista_de_pares):
    soma = 0
    for numero in lista_de_pares:
        if numero % 2 == 0:
            soma += numero
    print(f'A soma dos pares da {lista_de_pares} foi: {soma}')


soma_pares(sorteio())
