# numeros primos

num = int(input('Digite um valor: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print('O numero {} é PRIMO'.format(num))
else:
    print('O numero {} NÃO é PRIMO, ele foi dividido {}x'.format(num, cont))
