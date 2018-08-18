valores = list()
impares = list()
pares = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    res = str(input('Deseja continuar [S/N]: '))[0].upper()
    if res == 'N':
        break

for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'Os valores foram: {valores}')
print(f'Os valores pares foram: {pares}')
print(f'Os valores impares foram: {impares}')
