# Mega sena
from random import choice
from time import sleep


print('#' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('#' * 30)
jogo = []

cont = int(input('Quantos palpites deseja? 0 para sair: '))
print(f'Sorteando {cont} jogos')

while cont != 0:
    numeros = list(range(1, 61))

    for i in range(6):
        num = choice(numeros)
        jogo.append(num)
        numeros.remove(num)

    cont -= 1
    jogo.sort()
    sleep(1)
    print(jogo)
    jogo.clear()
  
print(f'{"BOA SORTE":^30}')