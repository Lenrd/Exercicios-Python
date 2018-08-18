# formas de pagamento

preco = float(input('Qual o valor do produto: '))
pag = int(input('Digite 1 para dinheiro/cheque\n'
                  'Digite 2 para cartão\n'
                  'Digite 3 para cartão até 2x\n'
                  'Digite 4 para cartão 3x ou mais '))

if pag == 1:
    print('PAGAMENTO EM DINHEIRO')
    novo = preco - (preco * 10 /100)
elif pag == 2:
    print('PAGAMENTO EM CARTÃO')
    novo = preco - (preco * 5 / 100)
elif pag == 3:
    print('PAGAMENTO EM 2X NO CARTÃO')
    novo = preco
elif pag == 4:
    print('PAGAMENTO EM 3X OU MAIS NO CARTÃO')
    novo = preco + (preco * 20 / 100)
else:
    novo = 'error'

print('O total a pagar é {}'.format(novo))
