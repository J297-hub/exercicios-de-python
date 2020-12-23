print('  10 TERMOS DE UMA PA     ')
primeiro=int(input('Primero termo: '))
razão=int(input('Razão: '))
termo=primeiro
cont=1
while cont <=10:
    print('{} > '.format(termo), end='')
    termo+=razão
    cont+=1
print('FIM')
