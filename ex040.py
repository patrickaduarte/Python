nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} a média é {:.1f}'.format(nota1, nota2, media))
if media <= 5:
    print('Média abaixo de 5.0: REPROVADO')
elif media < 7:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO')
else:
    print('Média 7.0 ou superior: APROVADO')
