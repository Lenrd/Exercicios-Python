# exercicios de classificação de dicionarios em Python
from random import randint
from time import sleep

print('EXERCICIOS DE CLASSIFICAÇÂO DE DICTS')
dados = dict()
for i in range(4):
    dados['jogador1'] = int(randint(1, 6))
    dados['jogador2'] = int(randint(1, 6))
    dados['jogador3'] = int(randint(1, 6))
    dados['jogador4'] = int(randint(1, 6))

for k, v in dados.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('-=-' * 10)

dados1 = sorted(dados, key = dados.get, reverse = True)
    

for c in dados1:
    print(f'O {c} tirou {dados[c]}')
    sleep(1)

