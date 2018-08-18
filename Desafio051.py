# prograssao aritmetica
ini = int(input('inicio da progressão: '))
raz = int(input('Razão da progressão: '))
soma = 0

# soma = ini + (fim - 1) * raz
for c in range(1, 11):
    soma = ini + (c - 1) * raz
    print(soma, end=' > ')
print('FIM')
# print('O primeiro termo da progressão é {} e o ultimo {}'.format(a1, an))
