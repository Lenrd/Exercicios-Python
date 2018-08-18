# somador supremo

c = 0
cont = 0
soma = 0
while c != 999:
    num = int(input('Digite um valor: '))
    if num == 999:
        c = 999
        cont - 1
        print('Fim')

    soma += num
    cont += 1

print('O total da soma foi {}'.format(soma))
print('A Quantidade de numeros foi {}'.format(cont))
