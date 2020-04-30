numero = int(input('''Digite um número para
calcular o seu Fatorial: '''))
controle = numero
print('Calculando o fatorial de {}! = {}'.format(numero, numero), end=' ')
while controle > 1:
    controle = controle - 1
    numero = numero * controle
    print('x {}'.format(controle), end=' ')
print('= {}'.format(numero))
