from time import sleep
print('{:=^40}'.format(' LOJAS LIMA '))
valor=float(input('Digite o valor do produto:'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] Á vista a dinheiro/cheque: 10% de desonto                                 
[ 2 ] Á vista cartão: 5% de desconto                                 
[ 3 ] 2x no cartão: preço normal                              
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opção= int(input('Selecione uma das opções:'))
print('PROCESSANDO...')
sleep(2)
if opção ==1:
    des1= valor - (valor*10)/100
    print('O Produto no valor de {} terá o valor final de R${}'.format(valor,des1))
elif opção ==2:
    des2= valor - (valor*5)/100
    print('O Produto no valor de {} terá o valor final de R${}'.format(valor,des2))
elif opção ==3:
    print('O produto terá o valor final de: R${}'.format(valor))
elif opção ==4:
    au= valor + (valor*20) /100
    print('O Produto no valor de {} terá o valor final de {}'.format(valor,au))
print('======= FIM ========')