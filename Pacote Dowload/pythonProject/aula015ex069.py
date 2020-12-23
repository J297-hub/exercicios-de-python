tot18=totH=totM20=0
print('------------------------------------')
print('       CADASTRE UMA PESSOA'  )
print('------------------------------------')
while True:
    id=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).upper().strip()
    next=str(input('Quer continuar? [S/N]')).upper().strip()
    if id >=18:
        tot18+=1
    if sexo=='M':
        totH+=1
    if sexo == 'F' and idade <20:
        totM20+=1
    if next =='N':
        break
print(f'{tot18} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {totH} homens.')
print(f'{totM20} mulheres tem menos de 20 anos.')
print('Fim do programa')

