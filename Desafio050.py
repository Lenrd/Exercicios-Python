# soma dos numeros pares
soma = 0
cont = 0
for i in range(1, 7):
    num = int(input('Diga {}° valor: '.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Soma é {}'.format(soma))
print('E o numero de pares é {}'.format(cont))
