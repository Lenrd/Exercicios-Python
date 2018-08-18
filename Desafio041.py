# categorias em natação
from datetime import date

print('*' * 8, 'CATEGORIAS', '*' * 8)
ano = int(input('Digite o ano de nascimento: '))
clas = date.today().year - ano

if clas <= 9:
    print('A categoria do aluno é MIRIM')
elif clas <= 14:
    print('A categoria do aluno é INFANTIL')
elif clas <= 19:
    print('A categoria do aluno é JUNIOR')
elif clas <= 20:
    print('A categoria do aluno é SENIOR')
else:
    print('A categoria do aluno é MASTER')
