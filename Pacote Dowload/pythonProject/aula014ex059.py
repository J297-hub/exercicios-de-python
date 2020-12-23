n1=int(input('Primeiro valor:'))
n2=int(input('Segundo valor:'))
opcao=0
while opcao !=5:
    print('''Opçôes de cálculo:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opcao=int(input('Escolha sua OPÇÃO:'))
    if opcao ==1:
        op1 = (n1 + n2)  # somar
        print('{}'.format(op1))
    elif opcao ==2:
        op2 = (n1 * n2)  # multiplicar
        print('{}'.format(op2))
    elif opcao ==3:
        if n1 > n2:
            print('Maior = {}'.format(n1))
        elif n2 > n1:
            print('Maior = {}'.format(n2))
    elif opcao ==4:
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opcao ==5:
        print('FIM do programa')
print('Fim')





