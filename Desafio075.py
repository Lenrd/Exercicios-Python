# le os valores pelo teclado e adiciona a uma tupla

lista = [] # lista que sera convertida em tupla

for num in range(4):
    n = int(input(f'Digite o {num + 1}º valor: '))
    lista.append(n)
numeros = (lista[0], lista[1], lista[2], lista[3])
print(f'O numero 9 aparece {numeros.count(9)} vezes.')  # conta a quantidade de noves
if 3 in numeros:
    print(f'O numero 3 aparece pela 1º vez na Pos: {numeros.index(3) + 1}')  # verifica e imprime se houver 3
else:
    print('O numero 3 não aparece na tupla')
for i in numeros:
    if i % 2 == 0:
        print(i, end=' ') # imprime numeros pares
