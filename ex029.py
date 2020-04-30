velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite de 80km/h')
    print('\033[31mVocê deve pagar uma multa de \033[33mR${:.2f}'.format((velocidade-80)*7))
print('\033[32mTenha um bom dia! Dirija com segurança!')

