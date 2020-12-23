lista=[]
pares=[]
impares=[]
while True:
    lista.append(int(input('Digite um número:')))
    next=str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if next in 'S':
        lista.append(int(input('Digite um número:')))
        next = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if next in 'N':
        break
for i,v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os valores digitados foram {lista}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')