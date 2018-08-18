# Desafio com o inicio 'santo'
cid = str(input('Digite o nome de uma cidade: ')).strip()
aux = cid.lower().split()
print('O nome da cidade começa con santo? ', aux[0] == 'santo'.lower())
