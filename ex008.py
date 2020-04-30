medida = float(input('Uma distância em metros: '))

print('A medida de {:.1f}m corresponde a\n{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(medida, (medida/1000), (medida/100), (medida/10), (medida*10), (medida*100), (medida*1000)))
