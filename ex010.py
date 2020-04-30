real = float(input('Quantos dinheiro você tem na carteira? R$ '))
dolar = real / 3.7393
euro = real / 4.2152

print('Com R$ {:.2f} você pode comprar US$ {:.2f} ou € {:.2f}'.format(real, dolar, euro))
