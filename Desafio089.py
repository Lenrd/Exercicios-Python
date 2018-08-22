alunos = list()

while True:

    aluno = list()
    notas = list()

    nome = str(input('Digite o Nome: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = (n1 + n2) / 2

    aluno.append(nome)
    notas.append(n1)
    notas.append(n2)
    notas.append(n3)
    aluno.append(notas)
    alunos.append(aluno[:])

    conf = str(input('Continuar? [S/N]'))[0].upper()
    while not 'SsNn':
        conf = str(input('Continuar? [S/N]'))[0].upper()
    
    if conf == 'N':
        break

print('-=-' * 10)
print(f'{"NUM":<5}{"NOME":<12}{"MÉDIA"}')
for a in range(len(alunos)):
    print(f'{str(a):<5}{alunos[a][0]:<12}{str(alunos[a][1][2])}')


while True:
    num = int(input('mostrar notas de qual aluno: '))

    print(f'{alunos[num][0]:<12}Nota1: {str(alunos[num][1][0]):<5}, nota2: {str(alunos[num][1][1])}')
