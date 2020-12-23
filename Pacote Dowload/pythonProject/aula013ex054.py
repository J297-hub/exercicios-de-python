from datetime import date
atual= date.today().year
totmaior=0
totmenor=0
for c in range (1,8):
    nasc = int(input('Em que ano a {} pessoa nasceu? :'.format(c)))
    atual= date.today().year
    anoatual=atual-nasc
    if anoatual <18:
        totmenor += 1
    elif anoatual >=18:
        totmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas de menor idade'.format(totmenor))
