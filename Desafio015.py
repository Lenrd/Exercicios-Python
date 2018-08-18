# Aluguel de carros
dia = int(input('Quantidade de dias em aluguel: '))
km = float(input('Quantidade de kilometros rodados: '))
taxa = (dia * 60) + (km * 0.15)
print('A Quantidade de dias foi:{}\nA quantidade de Km rodados foi:{} \nO total a pagar é:{:.2f}R$'.format(dia, km, taxa))
