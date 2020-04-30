numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um número de 0 à 10: '))
    if num >= 0 and num <= 10:
        break
print(f'Você digitou o número {numeros[num]}')
