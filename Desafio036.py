# calculo da compra da casa
print('+-' * 8, 'SEM FIM IMOVEIS', '-+' * 8)

valorcasa = float(input('Qual o valor da casa?R$ '))
salario = float(input('Qual o salario? '))
parcelas = int(input('Qual o numero de parcelas? '))
mensalidade = valorcasa / parcelas

if mensalidade <= salario * 30 / 100:
    print('Meus parabéns a mensalidade de {:.2f}R$ não exede os 30% do salario'.format(mensalidade))
else:
    print('O valor da parcela de {} exede os 30% do salario do comprador'.format(mensalidade))
