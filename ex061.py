print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 0
while cont < 10:
    print('{} ->'.format(primeiro), end=' ')
    primeiro = primeiro + razao
    cont += 1
print('ACABOU')
