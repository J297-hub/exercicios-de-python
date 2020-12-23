a1=('zero','um','dois','tres','quatro','cinco',
    'seis','sete','oito','nove','dez','onze',
    'doze','treze','quatorze','quinze','dezesseis',
    'dezessete','dezoito','dezenove','vinte')
while True:
    num=int(input('Digite um número entre 0 e 20: '))
    next = str(input('Deseja continuar? [S/N]: ')).upper()
    if num <0 and num >20:
        break
    while next in 'S':
        num = int(input('Digite um número entre 0 e 20: '))
        next = str(input('Deseja continuar? [S/N]: ')).upper()
    if next in 'Nn':
        break
print(f'Você digitou o número {a1[num]}')
