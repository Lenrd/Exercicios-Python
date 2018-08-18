# matriz 3x3

matriz = list()
maior = 0
soma = 0
soma3 = 0


for i in range(3):
    linha = list()
    for n in range(3):
        num = int(input('Digite um numero: '))
        linha.append(num)
    matriz.append(linha[:])
    linha.clear()
    
print('-=' * 15)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^3}]', end=' ')
    print('')

# soma os pares
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
            
# soma a terceira coluna
for i in range(3):
    soma3 += matriz[i][2]

# define o maior
for i in range(3):
    if matriz[1][i] > maior:
        maior = matriz[1][i]

# imprime os resultados
print('-=' * 15)
print(f'A soma dos pares é: {soma}')
print(f'A soma da 3ª coluna é: {soma3}')
print(f'O maior valor 2ª linha é: {maior}')
        
    