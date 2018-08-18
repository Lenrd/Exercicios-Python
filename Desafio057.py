# programa que le o gênero treinar while


sexo = str(input('Digite o Sexo, [M/F]  ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('DADO INVALIDO POR FAVOR APENAS [M/F]  ')).strip().upper()[0]

print('O sexo {}, adicionado com sucesso'.format(sexo))
