import random
from time import sleep
# usa .random pra fazer um jogo de advinhação

print('='*10, 'JOGO DE ADVINHAÇÂO', '='*10)
print('Pensando em um numero de 0 a 5. . .')
sleep(3)

cpu = int(random.randrange(6))
p1 = int(input('Dê o seu palpite: '))

if cpu == p1:
    print('Meus Parabéns!!! Você acertou')
else:
    print('Hum... Tente novamente!')
