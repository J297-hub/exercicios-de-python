print('Bem vindo ao IMC!')
peso=float(input('Qual o seu peso? (KG):'))
altura=float(input('Qual é a sua altura? (M):'))
imc= peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <18.5:
    print('ABAIXO DO PESO')
elif imc >=18.5 and imc <=25:
        print('PESO IDEAL')
elif imc >=26 and imc <=30:
    print('SOBREPESO')
elif imc >=31 and imc <=40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')



