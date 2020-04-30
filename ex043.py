peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.2f}. '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif imc < 25:
    print('Você está no PESO IDEAL.')
elif imc < 30:
    print('Você está com SOBREPESO.')
elif imc < 40:
    print('Você está OBESO.')
else:
    print('Você está com OBESIDADE MÓRBIDA')
