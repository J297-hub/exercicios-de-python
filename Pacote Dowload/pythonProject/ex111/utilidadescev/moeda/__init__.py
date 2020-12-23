def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print('-' * 30)


def aumentar (preço,taixa):
    res= preço + (preço * taixa /100)
    return res


def diminuir (preço, taixa):
    res= preço - (preço * taxa /100)
    return res


def dobro (preço, formato=False):
    res=preço * 2
    return res if formato is False else moeda(res)


def metade(preço, formato=False):
    res=preço /2
    return res if not formato else moeda(res)


def moeda (preço=0, moeda='R$'):
    return  f'{moeda}{preço:.2f}'.replace('.', ',')

