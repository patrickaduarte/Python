while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 30)
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num*cont}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
