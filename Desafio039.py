# verificação de alistamento
from datetime import date

idade = int(input('Digite o ano de nascimento: '))
ver = date.today().year - idade

if ver <= 17:
    print('Você ainda vai se alistar ')
    print('Faltam {} anos'.format(18 - ver))
elif ver == 18:
    print('Hora de se alistar ')
else:
    print('Já passou a hora do alistamento')
    print('Você está {} anos atrasado'.format(ver - 18))
