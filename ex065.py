continua = 'S'
somador = 0
contador = 0
while continua not in 'Nn':
    num = int(input('Digite um número: '))
    if contador == 0:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    somador += num
    contador += 1
    continua = str(input('Deseja continuar [S,N]: '))
print('Você digitou {} números e a média foi {:.2f}'.format(contador, somador/contador))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
