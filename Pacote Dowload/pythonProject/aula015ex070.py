total=totmil=smaller=cont=0
cheap=''
while True:
    name=str(input('Products name: '))
    cost=float(input('cost: $'))
    cont+=1
    total+=cost
    if cost>1000:
        totmil+=1
    if cont ==1 or cost <smaller:
        smaller=cost
        cheap=name
    next =' '
    while next not in 'SN':
        next = str(input('Want to continue? [S/N]: ')).strip().upper()[0]
    if next =='N':
        break
print(f'Total purchase were ${total:.2f}')
print(f'We have {totmil} products costing over $1000.00')
print(f'The cheapest product was {cheap} that is costs ${smaller:.2f}')
