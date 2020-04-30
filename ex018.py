import math

angulo = float(input('Digite o ângulo que você deseja: '))
angulo = math.radians(angulo)
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, math.sin(angulo)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, math.cos(angulo)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, math.tan(angulo)))
