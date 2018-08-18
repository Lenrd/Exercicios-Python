# imports
from random import randint

# par ou impar V2

#variaveis
cpu = randint(0, 10)
cont = 0

#codigo
print('=================PAR OU IMPAR==================')

while True:
    num = int(input('Digite um numero: '))
    escolha = str(input('Deseja par ou impar? [P ou I]: ')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Deseja par ou impar? [P ou I]: ')).upper().strip()[0]

    res = (cpu + num) % 2
    print(f'O CPU jogou {cpu} e o JOGADOR jogou {num}')
    print('=' * 50)
    if escolha == 'P':

        if res == 0:
            print('PAR: O jogador vence!')
            cont += 1

        else:
            print('IMPAR: O cpu vence')
            print(f'O numero de Vitorias foi {cont}')
            print('=' * 50)
            break
    else:

        if res == 1:
            print('IMPAR: O jogador vence!')
            cont += 1

        else:
            print('PAR: O cpu vence')
            print(f'O numero de Vitorias foi {cont}')
            print('=' * 50)
            break
