from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today()
idade = atual.year - nascimento

print('O atleta tem {} anos.'.format(idade))

if idade > 25:
    print('CLASSIFICAÇÃO: MASTER')
elif idade > 19:
    print('CLASSIFICAÇÃO: SÊNIOR')
elif idade > 14:
    print('CLASSIFICAÇÃO: JÚNIOR')
elif idade > 9:
    print('CLASSIFICAÇÃO: INFANTIL')
else:
    print('CLASSIFICAÇÃO: MIRIM')
