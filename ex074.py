import random

numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print('Os Valores sorteados foram: ', end='')
for num in range(0, len(numeros)):
    print(f'{numeros[num]}', end=' ')
for cont in range(0, len(numeros)):
    if cont == 0:
        menor = maior = numeros[cont]
    else:
        if numeros[cont] < menor:
            menor = numeros[cont]
        if numeros[cont] > maior:
            maior = numeros[cont]
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')