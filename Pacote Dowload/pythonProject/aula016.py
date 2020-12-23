#TUPLAS SÃO IMUTÁVEIS
lanche= ('hambúrguer','suco','pizza','pudim')
#for cont in range (0,len(lanche)):
    #print(f'Eu vou comer {lanche[cont]}')
#or comida in lanche:
    #print(f'Eu vou comer {comida}')
#print('Comi pra caramba!')
for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

