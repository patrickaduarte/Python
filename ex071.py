print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
ced5 = ced10 = ced20 = ced50 = ced100 = 0
valor = 1
while valor % 5 != 0:
    valor = int(input('Quanto você quer sacar? R$'))
while True:
    if valor >= 100:
        ced100 = valor / 100
        valor = valor % 100
    elif valor >= 50:
        ced50 = valor / 50
        valor = valor % 50
    elif valor >= 20:
        ced20 = valor / 20
        valor = valor % 20
    elif valor >= 10:
        ced10 = valor / 10
        valor = valor % 10
    elif valor >= 5:
        ced5 = valor / 5
        valor = valor % 5
    else:
        break
if ced100 != 0:
    print(f'Total de {int(ced100)} cédulas de R$100')
if ced50 != 0:
    print(f'Total de {int(ced50)} cédulas de R$50')
if ced20 != 0:
    print(f'Total de {int(ced20)} cédulas de R$20')
if ced10 != 0:
    print(f'Total de {int(ced10)} cédulas de R$10')
if ced5 != 0:
    print(f'Total de {int(ced5)} cédulas de R$5')
print('='*30)
print('Volte sempre ao BANCO CEV')
