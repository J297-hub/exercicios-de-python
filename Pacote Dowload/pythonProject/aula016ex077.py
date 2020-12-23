listagem=('ultimo',
          'heroi',
          'terra',
          'super',
          'xandao')
for l in listagem:
    print(f'\nNa palavra {l.upper()} temos ',end='')
    for letra in l:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')




