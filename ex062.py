print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 0
termos = 10
somador = 0
while termos != 0:
    while cont < termos:
        print('{} ->'.format(primeiro), end=' ')
        primeiro = primeiro + razao
        cont += 1
    print('PAUSA')
    somador += termos
    termos = int(input('Quantos termos você quer mostrar a mais: '))
    cont = 0
print('Progressão finalizada com {} termos mostrados'.format(somador))
