def aumentar (preço,taixa):
    res= preço + (preço * taixa /100)
    return res


def diminuir (preço, taixa):
    res= preço - (preço * taxa /100)
    return res


def dobro (preço):
    res=preço * 2
    return res


def metade(preço):
    res=preço /2
    return res


def triplo (preço):
    res= preço *3
    return res


def moeda (preço=0, moeda='R$'):
    return  f'{moeda}{preço:.2f}'.replace('.', ',')

