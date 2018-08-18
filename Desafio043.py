# calculo do imc versao sei la
massa = float(input('Massa corporal em KG: '))
altura = float(input('Altura em Metros: '))
imc = massa / (altura * altura)

if imc <= 18.5:
    print('Seu imc está em {:.1f}, você está abaixo do peso'.format(imc))
elif imc <= 25:
    print('Seu imc é de {:.1f}, e você está no peso ideal'.format(imc))
elif imc <= 30:
    print('Seu imc é de {:.1f}, e você está no Sobrepeso'.format(imc))
elif imc <= 40:
    print('Seu imc é de {:.1f}, e você está Obeso'.format(imc))
else:
    print('Seu imc é de {:.1f}, e Você está com OBESIDADE MÓRBIDA'.format(imc))
