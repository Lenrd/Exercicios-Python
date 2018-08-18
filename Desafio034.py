# calculo de salário
salario = float(input('Valor do salario: '))

if salario > 1250.0:  # define o salario e aumenta em 10%
    print('Seu novo salario é: {:.2f}'.format((salario * 0.1) + salario))
else: # define o salario e aumenta em 15%
    print('Seu novo salario é: {:.2f}'.format((salario * 0.15) + salario))
