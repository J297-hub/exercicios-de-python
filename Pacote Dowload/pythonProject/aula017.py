#num=[2,5,9,1]
#num[2]=3                    #na posiçao 2 vai mudar de 9 para virar 3
#num.append(7)               #estou adicionando o valor 7
#num.sort(reverse=True)      #ordem reversa
#num.insert(2,0)             #inseri um valor e reordena automaticamente o resto, na posição 2, vai inserir o valor 0
#num.pop(2)                  #vai tirar o valor que tem na posição 2
#num.insert(2,2)            #na posição 2 vou adicionar o valor 2
#num.remove(2)              #vai remover o primeiro 2
#if 4 in num:
 #   num.remove(4)
#else:
 #   print('Não achei o número 4')
#print(num)
#print(f'Essa lista tem {len(num)} elementos.')
valores=list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate (valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chegei ao final da lista')


