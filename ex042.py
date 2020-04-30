print('-='*15)
print('Analisador de triângulos')
print('-='*15)
flag = 0
lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))

if (lado1 > abs(lado2 - lado3) and lado1 < (lado3 + lado2)) and (lado2 > abs(lado1 - lado3) and lado2 < (lado1 + lado3)) and (lado3 > abs(lado1 - lado2) and lado3 < (lado2 + lado1)):
    print('Os segmentos acima PODEM FORMAR triângulo', end=' ')
    flag = 1
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

if flag == 1:
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')