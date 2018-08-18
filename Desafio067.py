# Tabuada V3.0
print('TABUADA V3')

# variaveis
cont = 1

# codigo
while True:
    print('=' * 50)
    num = int(input('De qual numero deseja saber a tabuada? '))
    if num < 0:
        print('O aplicativo tabuada foi encerrado, Por favor volte sempre!')
        break
    cont = 1
    while cont < 11:
        print(f'{num:2} x {cont:2} = {cont * num}')
        cont += 1
print('=' * 50)
