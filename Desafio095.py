jogador = dict()
jogadores = list()
gols = list()
total = 0

# bloco de coleção de dados
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))

    jogos = int(input('Quantidade de jogos: '))
    if jogos == 0:
        break

    for j in range(jogos):
        gols.append(int(input(f'Quantos gols na partida {j}: ')))
    jogador['gols'] = gols[:]
    gols.clear()
    
    for g in jogador['gols']:
        total += g
    jogador['total'] = total
    
    jogadores.append(jogador.copy())
    total = 0
    
    cont = str(input('Deseja continuar[s/n]: '))[0].upper()
    while cont not in 'SN':
        cont = str(input('Deseja continuar[s/n]: '))[0].upper()
    if cont == 'N':
        break

# bloco de estatisticas
print('-+-' * 20)
print(f'{"Cod":<3}{"Jogador":^20}{"Gols":<10}{"Total":^3}')
for i in range(len(jogadores)):
    print(f'{i:<3}{str(jogadores[i]["nome"]):^20}{str(jogadores[i]["gols"]):<10}{str(jogadores[i]["total"]):^3}')


while True:
    num = int(input('Qual jogador voce gostaria de saber sobre: '))
    print('-+-' * 20)
    print(jogadores[num])

    print('-+-' * 20)
    for k, v in jogadores[num].items():
        print(f'O campo {k} tem o valor {v}')

    jogos = len(jogadores[num]['gols'])

    print('-+-' * 20)
    print(f'O jogador {jogadores[num]["nome"]} jogou: {jogos} jogos')
    for j in range(jogos):
        print(f'No jogo {j} marcou {jogadores[num]["gols"][j]}')
    print(f'Num total de {jogadores[num]["total"]} gols.')


    cont = str(input('Deseja continuar[s/n]: '))[0].upper()
    while cont not in 'SN':
        cont = str(input('Deseja continuar[s/n]: '))[0].upper()
    if cont == 'N':
        break
