frase=str(input('Escreva uma frase:')).upper().strip()
print('Analisando...')
print('Nessa frase aparece {} vezes a letra A'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))



