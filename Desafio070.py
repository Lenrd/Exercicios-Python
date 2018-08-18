# estatistica de produto
total = caro = barato = 0
cont = 1
while True:
    print('+' * 50)
    nome = str(input('Nome do produto: ')).upper()
    preco = float(input('Digite o valor do produto me R$: '))
    print('+' * 50)

    if cont == 1:
        barato = preco
        nomebarato = nome
        cont += 1

    elif preco > 1000:
        caro += 1

    elif preco < barato:
        nomebarato = nome

    total += preco

    conf = str(input('Deseja continuar? [S/N]: ')).upper()
    while conf not in 'SN':
        conf = str(input('Deseja continuar? [S/N]: ')).upper()

    if conf == 'N':
        print('+' * 50)
        print(f'O total deu {total:.2f}, O produto mais barato foi {nomebarato} e tem {caro} produto mais caros que 1000R$')
        break
