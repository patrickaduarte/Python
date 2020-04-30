cont = 0
soma = 0
for c in range(3, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} números solicitados é {}'.format(cont, soma))
