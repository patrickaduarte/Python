import random
import time

print('\033[33m-=-'*20)
print('\033[34mVou pensar em um número de 0 à 5. Tente adivinhar...')
print('\033[33m-=-'*20)

numero = int(random.randint(0, 5))
escolha = int(input('\033[0;30mEm que número eu pensei? '))
print('\033[35mPROCESSANDO...')
time.sleep(2)
if escolha == numero:
    print('\033[33mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}.'.format(numero, escolha))

