valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    res = str(input('Deseja continuar [S/N]: '))[0].upper()
    if res == 'N':
        break
valores.sort(reverse=True)
print(f'Foram digitados: {len(valores)} numeros na lista.')
print(valores)
if 5 in valores:
    print(f'O valor 5 está na posição: {valores.index(5)}')
else:
    print('O valor 5 não se encontra na lista')
