num = int(input('Digite um número: '))
cont = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[33m{} '.format(i), end='')
        cont = cont + 1
    else:
        print('\033[31m{} '.format(i), end='')
print('\033[m\nO número {} foi divisível {} vezes'.format(num, cont))
print('E por isso ele ', end='')
if cont == 2:
    print('NÃO É PRIMO!')
else:
    print('É PRIMO!')
