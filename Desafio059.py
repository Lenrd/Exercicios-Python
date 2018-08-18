#somador while

op = 0
while op != 5:
    op = int(input("""[1] para somar
[2] para multiplicar
[3] para saber o maior
[4] para tentar outro numero
[5] para sair """))
    if op == 1:
        print('SOMA')
        a = int(input('Digite um valor: '))
        b = int(input('Digite outro valor: '))
        print('O resultado da SOMA é {}'.format(a+b))

    elif op == 2:
        print('MULTIPLICAÇÃO')
        a = int(input('Digite um valor: '))
        b = int(input('Digite outro valor: '))
        print('O resultado da MULTIPLIÇÃO é'.format(a * b))

    elif op == 3:
        print('QUAL O MAIOR')
        a = int(input('Digite um valor: '))
        b = int(input('Digite outro valor: '))
        if a > b:
            print('O primeiro valor é maior')
        else:
            print('O segundo valor é maior')
    elif op == 4:
        print('Insira outro valor')
    else:
        op = 5
print('Operação bem sucedida')