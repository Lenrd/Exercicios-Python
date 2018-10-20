#contador

import time

def contador():
    print('=' * 20)
    for i in range(1, 11):
        print(i, end=' ')
        time.sleep(0.5)
    print('Fim!')

    print('=' * 20)
    for i in range(10, 0, -1):
        print(i, end=' ')
        time.sleep(0.5)
    print('Fim!')

    print('=' * 20)
    inicio = int(input('Digite o numero inicial da contagem: '))
    fim = int(input('Digite o numero final da contagem: '))
    passo = int(input('Digite o passo da contagem :'))
    if inicio > fim:
        if passo == 0:
            passo = 1
        while inicio >= fim:
            print(inicio, end=' ')
            inicio -= passo
        print('Fim!')
    else:
        if passo == 0:
            passo = 1
        while inicio <= fim:
            print(inicio, end=' ')
            inicio += passo
        print('Fim!')

    


contador()
