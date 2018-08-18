# cabuloso
entrada = str(input('Digite uma expressão: ')).replace(' ','')
expressao = []

for i in entrada:
    expressao.append(i)
if expressao.count('(') != expressao.count(')'):
    print('Expressão invalida! ')
else:
    print('Expressão valida! ')
