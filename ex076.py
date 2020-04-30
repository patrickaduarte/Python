lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Trasferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('='*30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('='*30)
for cont in range(0, len(lista), 2):
    print('{:.<20}R${:>7.2f}'.format(lista[cont], lista[cont+1]))
print('='*30)
