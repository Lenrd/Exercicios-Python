alunos = list()

while True:

    aluno = list()
    notas = list()

    nome = str(input('Digite o Nome: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = n1 + n2 / 2

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

for a in alunos:
    print(a)
