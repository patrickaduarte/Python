num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma = soma + num
        cont += 1
print('Você digitou {} números e soma entre eles é {}'.format(cont, soma))
