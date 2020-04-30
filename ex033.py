num1 = input('Primeiro valor: ')
num2 = input('Segundo valor: ')
num3 = input('Terceiro valor: ')

if num1 > num2 and num1 > num3:
    maior = num1
    if num2 < num3:
        menor = num2
    else:
        menor = num3
if num2 > num1 and num2 > num3:
    maior = num2
    if num1 < num3:
        menor = num1
    else:
        menor = num3
if num3 > num2 and num3 > num1:
    maior = num3
    if num2 < num1:
        menor = num2
    else:
        menor = num1
print('O menor valor digitado foi {}'.format(menor))
print('O menor valor digitado foi {}'.format(maior))
