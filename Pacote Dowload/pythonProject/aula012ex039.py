from datetime import date
print('BEM VINDO AO ALISTAMENTO MILITAR BRASILEIRO!')
print(''' Selecione o seu sexo:
 [1] MASCULINO
 [2] FEMININO''')
opção=int(input('Sua opção foi:'))
anoatual = date.today().year
idade = anoatual - nasc
if opção ==2:
    print('Infelizmente você não pode realizar o alistamento militar obrigatório, tenha um bom dia!')
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, anoatual))
if opção ==2:
    print('Infelizmente você não pode realizar o alistamento militar obrigatório, tenha um bom dia!')
elif opção ==1 and idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo= 18 - idade
    print('Você ainda não tem 18 anos, faltam {} anos'.format(saldo))
else:
    print('Você já tem mais de 18 anos, sua época de alistamento já passou, não é possível servir mais.')
nasc = int(input('Ano de nascimento:'))


