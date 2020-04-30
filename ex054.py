from datetime import date
atual = int(date.today().year)
menor = 0
maior = 0
for i in range(1, 8):
    pessoa = int(input('Em que ano a {}ª nasceu? '.format(i)))
    pessoa = atual - pessoa
    if pessoa >= 21:
        maior += 1
    else:
        menor += 1
print('''Ao todo tivemos {} pessoas maiores de idade
E também {} pessoas menores de idade'''.format(maior, menor))
