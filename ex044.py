print('{:=^40}'.format(' LOJAS GUANABARA '))

valor = float(input('Preço das compras R$ '))
condicao = int(input('''FORMAS DE PAGAMENTO
[ 1 ] A vista dinheiro
[ 2 ] A vista no cartão
[ 3 ] Cartão em 2x
[ 4 ] Cartão parcelado
Informe aqui: '''))

if condicao == 1:
    print('Sua compra de R${:.2f} a vista no dinheiro fica por R${:.2f}'.format(valor, valor * 0.90))
elif condicao == 2:
    print('Sua compra de R${:.2f} a vista no cartão fica por R${:.2f}'.format(valor, valor * 0.95))
elif condicao == 3:
    print('Sua compra de R${:.2f} em duas vezes, fica R${:.2f} a parcela'.format(valor, valor / 2))
elif condicao == 4:
    parcela = int(input('Quantas parcelas: '))
    print('Sua compra de R${:.2f} em {} vezes, fica R${:.2f} a parcela, no total de {:.2f}'.format(valor, parcela, (valor*1.20) / parcela, valor * 1.20))
else:
    print('Forma de pagamento inválida, tente novamente')
