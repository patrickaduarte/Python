numero = int(input('Digite um número: '))

print('Analisando o número {}...'.format(numero))
print('Unidade: {}'.format((numero // 1) % 10))
print('Dezena: {:.0f}'.format((numero // 10) % 10))
print('Centena: {}'.format((numero // 100) % 10))
print('Milhar: {}'.format((numero // 1000) % 10))
