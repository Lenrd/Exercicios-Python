# maior em funcoes

def maior(*numeros):
    maior_num = numeros[0]
    for numero in numeros:
        if numero > maior_num:
            maior_num = numero
    print('=' * 40)
    print(f'Quantidade de numeros passados: {len(numeros)}')
    for numero in numeros:
        print(numero, end=' ')
    print('Fim!')
    print(f'O maior numero é: {maior_num}')
    print('=' * 40)


maior(12,15,32,78,2,5,7,5,99,32,100,1,2,35,2)
maior(1,2,3,42,1,3,4,2,45)
maior(2,42,1541,5436,37,312,3,4)