casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
financiamento = int(input('Quantos anos de fincanciamento: '))
parcela = float(casa / (financiamento * 12))

print('Para pagar uma casa de {:.2f} em {} anos prestação será de R${:.2f}'.format(casa, financiamento, parcela))

if parcela > (salario * 0.30):
    print('Empréstimo NEGADO')
else:
    print('Empréstimo pode ser CONCEDIDO')
