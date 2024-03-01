print('='*46)
print('{:^46}'.format('Analisador de Dados em uma Tupla'))
print('='*46)
num = (int(input('Digite o 1º número: ')),
       int(input('Digite o 2º número: ')),
       int(input('Digite o 3º número: ')),
       int(input('Digite o 4º número: ')))
print('='*46)
print(f'Valores Digitados: {num}')
print('='*46)
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes')
else:
    print(f'O Valor 9 NÃO foi digitado.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
elif 3 in num:
    print(f'O valor 3 apareceu nas {num.index(3)+1} posição')
elif 3 in num:
    print(f' e na {num.index(3)+1} posição e na'
          f'{num.index(3)+2} posição')
elif 3 in num:
    print(f' e na {num.index(3) + 1} posição e na'
          f'{num.index(3) + 2} posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares foram digitados ', end= ' ')
for n in num:
    if n % 2 == 0:
        print(n, end= '  ')
print('\n','='*46)