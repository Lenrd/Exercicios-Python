# brasileirão parça

times = ('Atlético-MG', 'Flamengo', 'Corinthians', 'Palmeiras', 'Fluminense', 'América-MG', 'São Paulo', 'Grêmio',
         'Vasco', 'Internacional', 'Botafogo', 'Sport', 'Cruzeiro', 'Vitória', 'Santos', 'Chapecoence', 'Atlético-PR', 'Bahia', 'Ceará', 'Paraná')
print(f'Os cinco melhores{times[:5]}')
print(f'Os quatro piores{times[16:]}')
print(f'Times na ordem alfabética{sorted(times)}')
print('O Chape tá na Pos {}'.format(times.index('Chapecoence')+1))
