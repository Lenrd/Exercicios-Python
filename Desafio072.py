# contador de zero a vinte

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))

    while num > 20 or num < 0:
        num = int(input('Valor incorreto, digite um numero entre 0 e 20: '))
    print(numeros[num])

    cont = str(input('Deseja continuar?[S/N]: ')).capitalize()[0]
    if cont != 'S':
        print('Volte Sempre!')
        break
