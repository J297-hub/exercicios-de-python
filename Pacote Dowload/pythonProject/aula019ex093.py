jogador= dict()
partidas=list()
jogador['nome']= str(input('Digite o nome do jogador: '))
tot=int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range( 0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}?: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partidas.')
for i,v in enumerate (jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')




