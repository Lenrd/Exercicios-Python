d = dict()

d['nome'] = str(input("Nome: "))
d['media'] = float(input('Média: '))


print(f'Nome é igual a {d["nome"]}')
print(f'Média é igual a {d["media"]}')
if d['media'] >= 7.0:
    print('A situacão do aluno é APROVADO')
else:
    print('A situação do aluno é REPROVADO')