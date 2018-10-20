#calculo de area

"""def calculo_area(largura, comprimento):
    area = largura * comprimento
    print(f'A area é {area}m²')


calculo_area(4.5, 8)"""

def calculo_area():
    print('Controle de terrenos')
    print('=' * 20)
    largura = float(input('Largura em M: '))
    comprimento = float(input('Comprimento em M: '))
    print(f'A área de um terreno {largura} x {comprimento} é de {largura * comprimento}.')


calculo_area()