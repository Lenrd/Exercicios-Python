# matriz 3x3

matriz = list()

for i in range(3):
    linha = list()
    for n in range(3):
        num = int(input('Digite um numero: '))
        linha.append(num)
    matriz.append(linha[:])
    linha.clear()
    

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^3}]', end=' ')
    print('')

