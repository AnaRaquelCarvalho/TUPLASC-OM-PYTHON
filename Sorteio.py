print('-'*46)
print('{:^46}'.format('SOTEIO com Mais números - Variáveis Compostas'))
print('{:^46}'.format('Coloca -se Parênteses '))
print('-'*46)
from time import sleep
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10),
           randint(1,10), randint(1,10), randint(1,10))
sleep(1)
print('Os valores sorteados foram: ',end= ' ')
for num in numeros:
    print(f'{num}', end= ' ')
print('\n','-'*46)