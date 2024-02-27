print('='*46)
print('{:^46}'.format('Campeonato Brasileiro 2023'))
print('='*46)
cont = 1
cont1 = 1
times = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG',
          'Bahia', 'Botafogo', 'Bragantino', 'Corinthians',
          'América-MG', 'Cuiabá', 'Flamengo', 'Fluminense',
          'Fortaleza', 'Grêmio', 'Internacional', 'Coritiba',
          'Palmeiras', 'São Paulo', 'Vasco', 'Cruzeiro',
          'Goias', 'Santos',)
print('{:^46}'.format('Tabela de Classificação'))
print('='*46)
for cont in range(1,len(times)):
    print(f'{cont}º  {times[cont]}')
print('='*46)
pos = ' '
print('{:^46}' .format('Os Cinco Primeiros colocados na Tabela'))
print(f'{times[0:5]}')
print('='*46)
print('{:^46}'.format('Os cinco últimos colocados'))
print(f'{times[-4:]}')
print('='*46)
print('{:^46}'.format('Clubes em ordem alfabética'))
print(f'{sorted(times)}')
print('='*46)
print('{:^46}'.format(f'O CORINTHIANS está na {times.index("Corinthians")} Posição'))
print('='*46)
