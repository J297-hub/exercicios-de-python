temp=[]
princ=[]
mai=men=0
while True:
    temp.append(str(input('Diga o nome da pessoa: ')))
    temp.append(float(input('Digite o peso da pessoa (Kg): ')))
    if len(princ) ==0:
        mai=men=temp[1]
    else:
        if temp [1] > mai:
            mai=temp[1]
        if temp[1] < men:
            men=temp[1]
    princ.append(temp[:])
    temp.clear()
    next=str(input('Deseja continuar? [S/N]: ')).upper()
    if next in 'N':
        break
print('-=' *30)
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi de {mai}KG. peso de ',end='')
for p in princ:
    if p[1] ==mai:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi de {men}KG. peso de ',end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ',end='')
print()