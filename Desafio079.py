# leia valores coleque-os sem contar os repetidos em sequencia.

lista = list()

while True:

    valor = int(input('Digite o valor: '))
    if valor in lista:
        print(f'Valor duplicado, não foi possivel adicionar')
    else:
        lista.append(valor)

    res = str(input('Deseja continuar [S/N]: ')).upper()  # verificação de continuidade
    if res == 'N':
        break

'''for i in lista:  # verifica i na lista e se o contador for maior que 1 ele deleta até sobrar um unico
    if lista.count(i) > 1:
        lista.remove(i)'''

lista.sort()  # ordena a lista
print(lista)
