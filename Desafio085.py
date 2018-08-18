numeros = [[], []]

for i in range(7):

    num = int(input('Digite um numero: '))

    if num % 2 == 0:
        numeros[0].append(num)  
    else:
        numeros[1].append(num)

numeros[1].sort()
numeros[0].sort()

print('-=' *40)
print(f'Os valores pares são {numeros[0]}')
print(f'Os valores impares são {numeros[1]}')
