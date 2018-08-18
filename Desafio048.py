# soma dos impares
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('Soma dos {} valores é igual a {},'.format(cont, soma), end=' ')
