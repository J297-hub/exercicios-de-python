from datetime import date
print('Bem vindo a confederação nacional de natação!')
nas=int(input('Digite seu ano de nascimento:'))
anoatual=date.today().year
idade= anoatual - nas
if idade <=9:
    print('MIRIM')
elif  idade >=10 and idade <=14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade >=15 and idade <=19:
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade ==20:
    print('CLASSIFICAÇÃO: SÊNIOR')
elif idade >20:
    print('CLASSIFICAÇÃO: MASTER')
print('Tenha um bom dia!')
