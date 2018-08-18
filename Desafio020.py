# Mais um na biblioteca random
from random import shuffle

'''alunos = 'Julio Carla Maria Lucas'.split()
random.shuffle(alunos)
print('A Ordem dos alunos é: {}'.format(alunos))'''
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

ordem = [n1, n2, n3, n4]
shuffle(ordem)
print('A nova ordem será...\n{}'.format(ordem))
