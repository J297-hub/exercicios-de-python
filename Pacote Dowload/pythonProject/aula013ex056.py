médiaidade=0
somaidade=0
idmenor=0
maisvelhohomem=0
nomevelho=''
for p in range (1,5):
    print('=-=-=- {} pessoa =-=-=-'.format(p))
    nome=str(input('NOME: ')).upper().strip()
    idade=int(input('IDADE: '))
    sexo=str(input('SEXO [M/F]: '))
    somaidade += idade
    if sexo in 'Ff' and idade <20:
        idmenor +=1
    if p ==1 and sexo in 'Mm':
        maisvelhohomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maisvelhohomem:
        maisvelhohomem=idade
        nomevelho=nome
médiaidade=somaidade /4
print('A média de idade dessas 4 pessoas é {}'.format(médiaidade))
print('O homem mais vélho tem {} anos e se chama {}'.format(maisvelhohomem,nomevelho))
print('{} mulheres tem menos de 20 anos'.format(idmenor))


