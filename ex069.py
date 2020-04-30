print('-'*40)
print('{:^40}'.format('CADASTRO DE PESSOA FISICA'))
print('-'*40)
homens = mulheres = maiores = 0
while True:
    sexo = ' '
    continuar = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 40)
    if idade >= 18:
        maiores += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    print('-' * 40)
    if continuar in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'Temos {mulheres} mulheres com menos de 20 anos.')
