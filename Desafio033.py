# maior e menor
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

menor = n1  # define o menor valor como n1 e verifica se há um menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

maior = n1  # define o maior valor como n1 e verifica se há um menor
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('O maior numero é {} e o menor numero é {}'.format(maior, menor))
