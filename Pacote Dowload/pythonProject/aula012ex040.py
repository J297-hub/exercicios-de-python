print('BEM VINDO AO BOLETIM ESCOLAR!')
nota1=float(input('Digite sua nota do primeiro semestre:'))
nota2=float(input('Digite sua nota do segundo semestre:'))
média=(nota1+nota2)/2
if  média >=5 and  média <7:
    print('O aluno está em RECUPERAÇÃO!')
elif  média > 7:
    print('APROVADO')



