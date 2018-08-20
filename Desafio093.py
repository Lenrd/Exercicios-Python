from random import randint
dados = dict()
gols = list()
cont = 0

dados['nome'] = str(input('nome: ')) 
part = int(input(f'Quantos jogos {dados["nome"]} jogou: '))

# gerencia quantidade de partidas e gols
for i in range(part):
    gol = randint(0, 3)
    gols.append(gol)
dados['gols'] = gols

print('-=-' * 12)
# faz a soma no contador
for num in dados['gols']:
    cont += num
dados['total'] = cont
print(dados)

print('-=-' * 12)
# cria a segunda parte do exercicio
for c, v in dados.items():
    print(f'O campo {c} tem o valor {v}')

print('-=-' * 12)
# dados finais tirados da lista do dicionario
print(f'O jogador {dados["nome"]} jogou {part} partidas')
for p in range(part):
    print(f'Na partida {p}, fez {dados["gols"][p]} gols')
