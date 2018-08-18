# conversor de bases numericas
print('Conversor de bases numericas')
num = int(input('Digite um numero: '))
op = int(input('Digite 1 para Binario, 2 para Octal e 3 para Hexadecimal: '))

if op == 1:
    print('Decimal > Binário')
    print('O valor de {} em decimal é igual a {} na base escolhida'.format(num, bin(num)[2:]))
elif op == 2:
    print('Decimal > Octal')
    print('O valor de {} em decimal é igual a {} na base escolhida'.format(num, oct(num)[2:]))
elif op == 3:
    print('Decimal > Hexadecimal')
    print('O valor de {} em decimal é igual a {} na base escolhida'.format(num, hex(num)[2:]))
else:
    print('error')
