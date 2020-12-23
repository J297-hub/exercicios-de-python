resp='S'
soma=quant=média=maior=menor=0
while resp in 'Ss':
    nu=int(input('Digite um número: '))
    soma+=nu
    quant+=1
    if quant ==1:
        maior=menor=nu
    else:
        if nu >maior:
            maior=nu
        if nu<menor:
            menor=nu
    resp=str(input('Quer continuar? [S/N]'))
média=soma/quant
print('Você digitou {} números e a média foi de {:.0f} '.format(quant,média))
print('\nO maior valor foi de {}'.format(maior))
print('\nO menor valor foi de {}'.format(menor))
