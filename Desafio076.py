# tabela de preços

# variaveis
tabela = ('lapis', 1.99, 'caneta', 2.40, 'Resma de papel', 15.60, 'regua', 4.00, 'apontador', 2.00, 'estojo', 9.00, 'livro', 123.43)

print('='*40)
for itens in range(0, len(tabela), 2):
    print(f'{tabela[itens]:.<20}R$: {tabela[itens + 1]:.2f}')
print('='*40)
