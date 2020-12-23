def ficha(nome='<desconhecido>', gols=0):
    if gols != '':
        for c in range(0, len(gols)):
            if gols[c] in 'abcdefghijklmnopqrstuvwxyz':
                True
        gols = 0
    if nome != '' and gols != '':
        return nome, gols
    elif nome != '' and gols == '':
        return nome, 0
    elif nome == '' and gols != '':
        return '<desconhecido', gols
    elif nome == '' and gols == '':
        return '<desconhecido>', 0


jogador = str(input('nome: ')).strip()
gol = str(input('quantos gols: ')).strip()
print(f'O jogador {ficha(jogador, gol)[0]} fez {ficha(jogador, gol)[1]} gol(s)')