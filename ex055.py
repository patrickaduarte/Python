maior = 0
peso = float(input('Qual é o peso da 1ª pessoa? '))
menor = peso
for i in range(2, 6):
    peso = float(input('Qual é o peso da {}ª pessoa? '.format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O menor peso lido foi de {:.1f}'.format(menor))
print('O maior peso lido foi de {:.1f}'.format(maior))
