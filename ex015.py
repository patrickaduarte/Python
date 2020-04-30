dias = float(input('Quantos dias alugados? '))
kilometros = float(input('Quantos Km rodados? '))

total = (dias * 60) + (kilometros * 0.15)
print('O total a pagar é de {:.2f}'.format(total))
