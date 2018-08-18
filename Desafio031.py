# Viagens
dis = float(input('Qual a distância da viagem em km/h? '))

if dis <= 200:
    preco = dis * 0.50
    print('A distância da viagem é {} e o valor é de {:.2f}R$ '.format(dis, preco))
else:
    preco = dis * 0.45
    print('A distância da viagem é {} e o valor é de {:.2f}R$ '.format(dis, preco))
