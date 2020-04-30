from datetime import date
nascimento = int(input('Ano de nascimento: '))
data = date.today()
idade = int(data.year) - nascimento
print('Quem nasceu em {} tem {} em {}.'.format(nascimento, idade, data.year))

if (idade > 18):
    print('''Você já deveria ter se alistado há {} anos.
Seu alistamento foi em {}.'''.format(idade - 18, nascimento + 18))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
else:
    print('''Ainda faltam {} anos para o alistamento.
Seu alistamento será em {}.'''.format(18 - idade, nascimento + 18))
