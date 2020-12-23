print('===============================================================')
times=('Internacional','Atlético-MG','São Paulo','Vasco',
        'Flamengo','Palmeiras','Santos','Fluminense','Ceará',
        'Fortaleza','Atético-GO','Grêmio','Atlético-PR','Sport',
        'Corinthias','Bahia','Botafogo','Chapecoense','Coritiba','Bragantino')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os últimos 4 colocados são {times[-4:]}')
print(f'Os times em ordem alfábética são {sorted(times)}')
print(f'Chapecoense está na posição {times.index("Chapecoense")+1} posicão')
