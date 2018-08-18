# O retorno do PA
cont = 1
ini = int(input('Digite o numero inicial: '))
raz = int(input('Digite a razão da prograsão: '))
fim = int(input('Digite o numero final: '))

while cont < fim + 1:
    res = ini + (cont - 1) * raz
    print(res, end=' > ')
    cont += 1
print('FIM')