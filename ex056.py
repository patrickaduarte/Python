hvelho = 0
nhvelho = ''
media = 0
mnovas = 0
for i in range(1, 5):
    print('-'*10, ' {}ª PESSOA '.format(i), '-'*10)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media += idade
    if sexo == 'M' and idade > hvelho:
        hvelho = idade
        nhvelho = nome
    if idade < 20 and sexo == 'F':
        mnovas += 1
media /= 4
print('A media de idade do grupo é {:.1f}.'.format(media))
print('O homem mais velho tem {} anos e o nome dele é {}.'.format(hvelho, nhvelho))
print('Ao todo são {} mulhere(s) com menos de 20 anos.'.format(mnovas))
