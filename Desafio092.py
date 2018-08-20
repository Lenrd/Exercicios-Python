from datetime import date

pessoa = dict()

pessoa['nome'] = str(input('Digite o nome: '))
pessoa['idade'] = abs(date.today().year - int(input('Digite o ano de nascimento: ')))
pessoa['ctps'] = int(input('Digite o numero da CTPS: '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = int(input('Digite o salario: '))
    pessoa['Aposentadoria'] = (pessoa['contratacao'] + 35) - (date.today().year - pessoa['idade'])
print('-=-' * 20)

for chave, valor in pessoa.items():
    print(f'{chave} tem o valor {valor}')
