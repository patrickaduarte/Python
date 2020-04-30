numeros = (int(input(f'Digite 1º número: ')), int(input(f'Digite 2º número: ')), int(input(f'Digite 3º número: ')), int(input(f'Digite 4º número: ')))
flag1 = 0
flag2 = 0
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
for j in range(0, len(numeros)):
    if numeros[j] == 3:
        flag1 = 1
if flag1 == 1:
    print('O primeiro valor 3 aparece na {}º posição'.format(numeros.index(3)+1))
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for cont in range(0, len(numeros)):
    if numeros[cont] % 2 == 0:
        if flag2 == 0:
            print('Os números pares digitados foram: ', end='')
            flag2 = 1
            print('{} '.format(numeros[cont]), end='')
        else:
            print('{} '.format(numeros[cont]), end='')
if flag2 == 0:
    print('Nenhum número par foi digitado.')



