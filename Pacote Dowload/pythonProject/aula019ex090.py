jogador=dict()
barcelona=('espanhol')
juventus=('italiano')
print('------  Descubra a nacionalidade de seus jogadores preferidos!  ------')
jogador['Nome']= str(input('Nome do jogador: ')).lower().strip()
jogador['clube']= str(input('Clube do jogador: ')).lower().strip()
if jogador['clube'] == barcelona:
    print(f'{"Nome"} que joga no Barcelona é {barcelona}!')
elif jogador['clube'] == juventus:
    print(f'{"nome"} que joga na Juventus é {juventus}!')
print('-='*30)


