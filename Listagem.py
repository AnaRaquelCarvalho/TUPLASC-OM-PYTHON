print('='*44)
print('{:^46}'.format('LISTAGEM DE PREÇOS  FORMATADO - TUPLAS'))
print('='*44)
listagem = ('Detergente', 1.50,
            'Bolacha', 4,
            'Chocolate', 10,
            'Arroz', 40,
            'Óleo', 4.50,
            'Açucar', 20)

print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*44)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('='*44)