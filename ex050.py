somador = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite o número {}: '. format(c+1)))
    if num % 2 == 0:
        somador = somador + num
        cont = cont + 1
print('Você informou {} números PARES e a soma foi {}.'.format(cont, somador))
