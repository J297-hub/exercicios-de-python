time=list()
jogador= dict()
partidas=list()
while True:
    jogador.clear()
    jogador['nome']= str(input('Digite o nome do jogador: '))
    tot=int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    partidas.clear()
    for c in range( 0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:#! / usr / bin / env python
"" "Utilitário de linha de comando do Django para tarefas administrativas." ""
importar os
import sys


def main ():
     "" "Executar tarefas administrativas." ""
     os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'helloworld.settings')
     tentar:
         de django.core.management import execute_from_command_line
     exceto ImportError como exc:
         raise ImportError (
             "Não foi possível importar Django. Você tem certeza que está instalado e"
             "disponível em sua variável de ambiente PYTHONPATH? Você"
             "esqueceu de ativar um ambiente virtual?"
         ) de exc
     execute_from_command_line (sys.argv)


if __name__ == '__main__':
     a Principal()
        resp=str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N ')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>4}',end='')
    for d in  v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca= int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca ==999:
        break
    if busca >=len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]}:')
        for i,g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE! >>')