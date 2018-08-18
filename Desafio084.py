dados = list()
temp = list()
pesado = list()
leve = list()
cont = 0
while True:

    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    dados.append(temp[:])
    temp.clear()

    cont += 1
    conf = str(input('Deseja continuar? [S/N]'))[0].upper()
    if conf == 'N':
        break

for p in range(len(dados)):
    if dados[p][1] >= 100:
        pesado.append(dados[p])
    elif dados[p][1] <= 70:
        leve.append(dados[p])

print(f'Foram {lendados} pessoas cadastradas:{dados}')
print(f'As mais pesadas foram {pesado}')
print(f'As mais leves foram: {leve}')

