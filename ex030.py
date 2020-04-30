numero = int(input('\033[35mMe diga um número qualquer: \033[m'))

if (numero % 2) == 0:
    print('O número {} é \033[34mPAR\033[m.'.format(numero))
else:
    print('O número {} é \033[34mIMPAR\033[m.'.format(numero))
