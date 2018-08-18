# le as retas e verifica se um triangulo pode ser formado
print('-*-' * 5, 'ANALISADOR DE TRIANGULOS', '-*-' * 5)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2): # condiçao que determina se o triangulo é valido
    print('Um triangulo pode ser formado')
else:
    print('Não pode se formar um triangulo com essas retas')
