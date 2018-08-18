from datetime import date
# anos bissextos
ano = int(input('Digite o ano, 0 para o ano atual: '))
print('Verificando. . .')
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 400 == 0:
    print('O ano {} é um ano bissexto'.format(ano))
else:
    print('O ano {} não é um ano bissexto'.format(ano))
