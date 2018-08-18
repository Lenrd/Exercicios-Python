# vogais em palavras

# variaveis

palavras = ('carro', 'casa', 'pessoa', 'lugar', 'aprender', 'python', 'você', 'consegue')


print('Vogais em palavras')
print('=' * 40)

for p in palavras:  # para palavras na tupla palavras
    print(f'Na palavra {p} temos:', end=' ')  # imprime as palavras
    for letra in p:  # para letras nas palavras
        if letra in 'aeiou':  # se as letras estiverem dentro de AEIOU
            print(letra, end=' ')  # imprima as letras
    print('')  # pula uma linha
