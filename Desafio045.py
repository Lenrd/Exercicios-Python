# jan ken po!
from random import randint
escolhas = ('pedra', 'papel', 'tesoura')
c1 = randint(0, 2)
p1 = int(input('''Opções...
[0] PEDRA
[1] PAPEL
[2] TESOURA'''))

print('O jogador escolheu {} e o CPU escolheu {}'.format(escolhas[p1], escolhas[c1]))

if escolhas[p1] == 'pedra' and escolhas[c1] == 'tesoura':
    print('Jogador ganha')

elif escolhas[p1] == 'papel' and escolhas[c1] == 'pedra':
    print('Jogador ganha')

elif escolhas[p1] == 'tesoura' and escolhas[c1] == 'papel':
    print('jogador ganha')

elif escolhas[c1] == 'pedra' and escolhas[p1] == 'tesoura':
    print('O cpu ganha')

elif escolhas[c1] == 'papel' and escolhas[p1] == 'pedra':
    print('O cpu ganha')

elif escolhas[c1] == 'tesoura' and escolhas[p1] == 'papel':
    print('O cpu ganha')

elif escolhas[c1] == escolhas[p1]:
    print('EMPATE')

else:
    print('ERROR, Opção inválida')
