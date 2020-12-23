from time import sleep
from random import randint
comp=randint(0,10)
print('''Sou seu computador....
Acabei de pensar em um número entre 0 e 10
Você consegue adivinhar qual é?''')
palpites=0
acertou=False
print('PROCESSANDO...')
sleep(2.5)
while not acertou:
    jogador = int(input('QUAL É O SEU PALPITE? :'))
    palpites += 1
    if jogador ==comp:
        acertou=True
        print('ACERTOU!')
print('Foram necessários {} palpites para acertar'.format(palpites))
