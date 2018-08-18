# leia 5 valores guarde em lista e mostre o maior e o menor

# code

valores = []  # lista
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a pos {i}: ')))  # adiciona valores a lista
print(valores)
print('=-' * 20)

print(f'O maior valor é:{max(valores)} e aparece nas Pos:', end=' ')
for i in range(len(valores)):  # verifica a lista e acha o maior
    if valores[i] == max(valores):
        print(i, end='...')

print('')  #pula uma linha

print(f'O menor valor é:{min(valores)} e aparece nas Pos:', end=' ')
for i in range(len(valores)):  # verifica e acha o menor
    if valores[i] == min(valores):
        print(i, end='...')