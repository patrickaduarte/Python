import random
vitorias = 0
print('-='*20)
print(f'VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
while True:
    opcao = ' '
    computador = random.randint(1, 10)
    jogador = int(input('Diga um valor: '))
    while opcao not in 'IP':
        opcao = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    resultado = computador + jogador
    print('-'*40)
    if opcao in 'I' and resultado % 2 != 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} DEU IMPAR')
        vitorias += 1
    elif opcao in 'P' and resultado % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} DEU PAR')
        vitorias += 1
    else:
        break
    print('-' * 40)
    print('Você VENCEU')
    print('Vamos jogar novamente')
    print('-=' * 20)
if resultado % 2 == 0:
    print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} DEU PAR')
else:
    print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado} DEU IMPAR')
print(f'GAME OVER! Você venceu {vitorias} vezes.')
