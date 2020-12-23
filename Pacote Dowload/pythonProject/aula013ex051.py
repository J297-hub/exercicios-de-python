print('=--=---=-=-=-=-=-=-----=-=')
print('  10 TERMOS DE UMA PA     ')
print('=--=---=-=-=-=-=-=-----=-=')
a1=int(input('Primero termo: '))
a2=int(input('Razão: '))
décimo= a1 + (10-1) * a2
for c in range (a1 , décimo+a2 , a2):
    print(c, end=' ')
print('\nAcabou')


