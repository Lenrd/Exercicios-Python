# jogo de advinhação numero 2
from random import randint
from time import sleep

print('========JOGO DE ADVINHAÇÃO VERSÃO 2.0========')
cpu = randint(0, 10)
print('Estou pensando em um numero... entre 0 e 10')
sleep(1)
j1 = int(input('Diga o seu paupite: '))
cont = 1

while j1 != cpu:
    j1 = int(input('Foi bem perto, tente outra vez: '))
    cont += 1

print('Muito bem! eu estava pensando no Nº {}'.format(cpu))
print('Você tentou {} vezes'.format(cont))
