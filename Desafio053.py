# palindromos frases que de traz pra frente são iguais

frase = str(input('Digite uma frase: ')).replace(' ', '').lower()
cont = len(frase)
avesso = str('')

for c in range(cont-1, -1, -1):
    avesso += frase[c]

if avesso.lower() == frase:
    print('A frase {} é um polindromo de {}'.format(avesso, frase))
else:
    print('A frase {} não é um palindromo de {}'.format(avesso, frase))
