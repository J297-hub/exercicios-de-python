from random import randint
itens= ('PEDRA' , 'PAPEL' , 'TESOURA')
compu= randint(0, 2)

print('=-=-=-=-=- BEM VINDO!! =-=-=-=-=-')
print('Vamos jogar JO KEN PÔ!')
print(''' 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
opção=int(input('Qual é a sua jogada?:))
if opção