# media mais elaborada
print('*' * 8, 'MEDIA', '*' * 8)
n1 = float(input('Primeira prova: '))
n2 = float(input('Segunda prova: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('Aluno reprovado com média {}'.format(media))
elif media <= 6.9:
    print('Aluno em recuperação com média {}'.format(media))
else:
    print('Aluno aprovado com média {}'.format(media))
