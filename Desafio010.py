# calcula em m2 a parede e quanta tinta precisa
alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = lar * alt
print('A area a ser coberta é de {}m²\nA quantidade de litros de tinta é {}l'.format(area, area/2))
