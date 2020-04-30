sexo = str(input('Informe o sexo: [S/M]')).upper().strip()[0]

while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, informe o sexo: [S/M]')).upper().strip()[0]
print('Sexo {} cadastrado com sucesso.'.format(sexo))
