# O app do conversor de dolares
real = float(input('Digite o valor em reais:R$ '))
dolar = float(input('Digite a cotação do dolar:USD '))
quant = real / dolar
print('O valor da conversão em dolar é {:.2f} USD'.format(quant))
