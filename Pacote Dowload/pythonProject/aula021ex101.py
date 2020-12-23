def voto (ano):
    from datetime import date
    anoatual=date.today().year
    idade=anoatual-ano
    if idade < 16:
        return f'Com idade de {idade} anos, VOTO NEGADO!!.'
    elif idade == 16 or idade >65:
        return f'Com idade de {idade} anos, VOTO OPCIONAL!!.'
    elif idade >=17 and idade <65:
        return f'Com a idade de {idade} anos, VOTO OBRIGÁTÓRIO!!.'


#Programa Principal
nasc=int(input('Ano de nascimento: '))
print(voto(nasc))
