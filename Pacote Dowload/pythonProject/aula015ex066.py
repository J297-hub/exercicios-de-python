soma=0
cont=0
while True:
    num=int(input('Digite um valor (999 para parar): '))
    if num ==999:
        break
    cont = cont+1
    soma = soma + num
print(f'A soma dos {cont} valores foi {soma}.')
print('FIM')