lista=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    next=str(input('Quer continuar? [S/N]: ')).strip().upper()
    if next == 'S':
        lista.append(int(input('Digite um valor: ')))
        next = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if next == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores')
print(f'A lista de valores na ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')