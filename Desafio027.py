# desafio do peimeiro e ultimo nome
nome = str(input('Digite seu nome completo: ')).strip()
ver = nome.split()
print('O nome seu primeiro nome é {}, é o ultimo {}'.format(ver[0], ver[len(ver)-1]))
