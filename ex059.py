from time import sleep

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('='*10, ' MENU ', '='*10)
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR''')
    opcao = int(input('>>>>Qual a sua opção? '))
    sleep(1)
    if opcao == 1:
        print('A soma entre {} e {} é igual a {}'.format(num1, num2, num1 + num2))
        sleep(1)
    elif opcao == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(num1, num2, num1 * num2))
        sleep(1)
    elif opcao == 3:
        if num1 > num2:
            print('O maior é {}'.format(num1))
            sleep(1)
        elif num1 < num2:
            print('O maior é {}'.format(num2))
            sleep(1)
        else:
            print('Os números são iguais!')
            sleep(1)
    elif opcao == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        sleep(1)
    elif opcao != 5:
        print('Opção inválida, digite novamente')
        sleep(1)
print('Finalizando...')
sleep(2)
print('='*30)
print('Fim do programa, volte sempre')
