import random
import time
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('''Sua opção: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

computador = random.randint(0, 2)
if (computador == 0 and jogador == 1) or (computador == 1 and jogador == 2) or (computador == 2 and jogador == 0):
    vencedor = str('JOGADOR')
elif (computador == 1 and jogador == 0) or (computador == 0 and jogador == 2) or (computador == 2 and jogador == 0):
    vencedor = str('COMPUTADOR')
elif jogador == computador:
    print('-=' * 15)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 15)
    print('FOI EMPATE!')
    exit()
else:
    print('Opção de jogada inválida, tente novamente')
    exit()

print('-='*15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*15)
print('{} VENCE'.format(vencedor))
