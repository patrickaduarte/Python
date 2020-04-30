print('{:^21}'.format('-'*25))
print('{:^26}'.format('Sequência de Fibonacci'))
print('{:^21}'.format('-'*25))
n = int(input('Quantos termos você quer mostrar? '))
fibo = 0
aux = 1
i = 0
while i < n:
    print(fibo, '-> ', end='')
    fibo = fibo + aux
    aux = fibo - aux
    i += 1
print('FIM')
