distancia = float(input('Qual é a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distancia))

if distancia <= 200:
    print('E o preço da sua passagem será R${:.2f}'.format(distancia*0.50))
else:
    print('E o preço da sua passagem será R${:.2f}'.format(distancia*0.45))
