# verificação de maioridade
from datetime import date

cont = 0

for i in range(1, 8):
    ano = int(input('em que ano {i}° pessoa nasceu ? '))
    ver = date.today().year - ano
    if ver >= 21:
        cont += 1
print('O nomero de maiores de idade é {}'.format(cont))
