print('='*46)
print('{:^46}'.format('LISTAGEM DE PREÇOS - TUPLAS'))
print('='*46)
listagem = (('  Detergente .................R$ 1,50'),
            ('  Bolacha ....................R$ 4,00'),
            ('  Chocolate ..................R$ 10,00'),
            ('  Arroz ......................R$ 40,00'),
            ("  Óleo........................R$ 4,50"),
            ('  Açucar......................R$ 20,00'))
for lista in listagem:
    print(f'{lista}')
print('='*46)