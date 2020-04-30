print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

for cont in range(0, 10, 1):
    print('{} ->'.format(primeiro), end=' ')
    primeiro = primeiro + razao
print('ACABOU')
