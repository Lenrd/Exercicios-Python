# final do while
conf = 'S'
cont = 0
soma = 0
while conf == 'S':

    num = int(input('Digite um valor: '))
    if cont == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    soma += num
    cont += 1
    conf = str(input('Deseja continuar? S/N: ')).upper()

print('A media dos valores foi {}'.format(soma/cont))
print('O maior valor foi {}, e o menor valor foi {}.'.format(maior, menor))
