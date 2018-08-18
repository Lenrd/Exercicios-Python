# tabuada 2.0
print('TABUADA 2.0')
num = int(input('Digite o numero para saber a tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
