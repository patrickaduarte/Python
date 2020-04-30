print('-'*40)
print('{:^40}'.format('LOJAS SUPER BARATO'))
print('-'*40)
caros = soma = barato = 0
maisbarato = ' '
while True:
    continuar = ' '
    produto = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço: '))
    if soma == 0:
        barato = preco
        maisbarato = produto
    else:
        if preco < barato:
            barato = preco
            maisbarato = produto
    soma += preco
    if preco >= 1000:
        caros += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
    print('-' * 40)
print(f'Total da compra foi R${soma:.2f}')
print(f'Temos {caros} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {maisbarato} que custou R${barato:.2f}.')
