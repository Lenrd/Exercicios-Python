# cadastro de pessoas
# variaveis
maioridade = homem = mulher = 0

# codigo
while True:
    # bloco de cadastro
    print('-' * 30, '\n      CADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper()

    if sexo == 'M'or 'F' and idade > 18:
        maioridade += 1

    if sexo == 'F' and idade < 20:
        mulher += 1

    if sexo == 'M':
        homem += 1
    print(f'Pessoa do sexo {sexo} cadastrado com sucesso!')

    # bloco de confirmação
    conf = str(input('Deseja continuar? [S/N]: ')).upper()
    print('-' * 30)
    while conf not in 'SN':
        conf = str(input('Deseja continuar? [S/N]: ')).upper()
        print('-' * 30)

    if conf == 'N':
        print(f'{maioridade} são MAIORES de idade\n'
              f'{homem} pessoas são HOMENS\n'
              f'{mulher} mulheres ABAIXO DE 20 anos')
        break
