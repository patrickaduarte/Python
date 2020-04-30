from random import randint
numero = randint(0, 10)
tentativas = 1
print('''Olá eu sou o seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
palpite = int(input('Qual é o seu palpite? '))
if numero == palpite:
    print('PARABÉNS, você acertou na primeira tentativa!')
else:
    while palpite != numero:
        if numero > palpite:
            print('Mais...Tente mais uma vez.')
            palpite = int(input('Qual é o seu palpite? '))
        else:
            print('Menos...Tente mais uma vez.')
            palpite = int(input('Qual é o seu palpite? '))
        tentativas += 1
    print('PARABÉNS, você acertou na {}ª tentativa!'.format(tentativas))
