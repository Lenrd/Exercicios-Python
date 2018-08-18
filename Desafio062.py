# The PA strikes back

cont = 1

ini = int(input('Digite o numero inicial: '))
raz = int(input('Digite a razão: '))
ter = 10
while cont < ter + 1:
    print(ini)
    if ini != 0:
        ini += raz

    if cont == ter:
        ter = ter + int(input('Quantos termos ainda gostaria de ver?  '))
    cont += 1

print('A operação foi finalizada com {} termos mostrados'.format(cont - 1))
