valor = float(input('Qual é o preço do produto? R$ '))
desconto = valor * 0.95

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(valor, desconto))
