# Exercicio 64 refeito

# variaveis inicializadas
soma = cont = 0

# codigo
print('=======SOMADOR INFINITO=======')
print('DIGITE 999 PARA SAIR')
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('*=' * 8, 'RESULTADO', '=*' * 8)
print(f'Foram {cont} valores digitados é a soma entre eles deu {soma}.')
