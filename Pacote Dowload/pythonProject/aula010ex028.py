from random import randint
from time import sleep
print('Vamos jogar um jogo!')
print('-=-' *20)
print('O computador gerará automaticamente um número entre 0 e 5, e você terá que adivinhar qual é!')
print('-=-' *20)
num=int(input('Escreva o número que você tentou adivinhar:'))
maq=randint(0,5)
print('-=-' *20)
print('PROCESSANDO...')
sleep(3)
print('O número que a maquina escolheu foi: {}'.format(maq))
if num == maq:
    print('Parabéns,você acertou!!!')
else:
    print('Infelizmente você errou')
print('\033[0;31;43mTHE END')





