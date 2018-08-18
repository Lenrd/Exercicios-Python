# multa por velocidade
vel = float(input('Velocidade do carro:km/h '))

if vel > 80.0:
    taxa = (vel - 80) * 7.00
    print('Você está acima da velocidade...')
    print('Sua multa foi de {:.2f}R$'.format(taxa))
else:
    print('Parabens! Você está na velocidade permitida')
