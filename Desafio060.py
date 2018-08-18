# fatorial boladao
from math import factorial
cont = 'S'

while cont == 'S':
    num = int(input('Digite um valor: '))
    print('O fatorial de {}! é {}'.format(num, factorial(num)))
    cont = str(input('Deseja tentar outro numero [S/N]: ')).upper()

print('Obrigado por usar nosso APP')
