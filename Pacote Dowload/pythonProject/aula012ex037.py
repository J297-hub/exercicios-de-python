from time import sleep
num=int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO    
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção=int(input('Sua opção: '))
print('PROCESSANDO...')
sleep(2)
if opção == 1:
    print('{} convertido para BINÁRIO é igual á {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual á {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. TENTE NOVAMENTE')
