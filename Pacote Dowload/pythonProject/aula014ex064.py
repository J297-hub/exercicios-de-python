nu=cont=soma=0
nu=int(input('Digite um número [999 para parar]: '))
while nu !=999:
    soma+=nu
    cont+=1
    nu = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} números e a soma entre eles é {}'.format(cont,soma))
print('FIM DO PROGRAMA')