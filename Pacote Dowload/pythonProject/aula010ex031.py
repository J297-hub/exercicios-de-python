dist=float(input('Digite a distância da viagem percorrida em Km:'))
print('Você irá iniciar uma viagem de {} km'.format(dist))
if dist<=200:
    preço=dist*0.50
else:
    preço=dist*0.45
print('O preço da passagem será de R$:{:.2f}'.format(preço))
