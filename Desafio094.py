pessoa = dict()
pessoas = list()
idacima = dict()
mulheres = 0
idade = 0


while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: '))[0].upper()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())

    if pessoa['sexo'] == 'F':
        mulheres += 1
    
    conf = str(input('Deseja continuar[S/N]: '))[0].upper()

    while conf not in 'NnSs':
        conf = str(input('Deseja continuar[S/N]: '))[0].upper()

    if conf == 'N':
        break

for i in range(len(pessoas)):
    idade += pessoas[i]['idade']
media = idade/len(pessoas)

for p in pessoas:
    if p['idade'] > media:
        idacima = p

print(f'A Quantidade de pessoas foi {len(pessoas)}.')
print(f'A media de idade é {media}')
print(f'A quantidade de mulheres é {mulheres} ', end=': ')
for m in range(len(pessoas)):
    if pessoas[m]['sexo'] == 'F':
        print(f'{pessoas[m]["nome"]}', end=' ')
    print('')

if len(idacima) != 0:
    for k, v in idacima.items():
        print(f'{k} = {v}', end='; ')

