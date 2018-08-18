# maior e menor
maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input('Insira o peso em Kg:'))
    if peso > maior:
        if i == 0:
            menor = peso
        maior = peso
    elif peso < menor:
        menor = peso

print('O MAIOR peso é {}, e o MENOR peso é {}.'.format(maior, menor))
