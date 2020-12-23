sexo=str(input('Sexo [F/M]: ')).upper().strip()
while not sexo in 'FM':
    print('Dado incorreto.TENTE NOVAMENTE!')
    sexo = str(input('Sexo [F/M]: ')).upper().strip()
print('FIM')
