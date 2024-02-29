print('-'*46)
print('{:^46}'.format('SOTEIO de 1 Número - Variável Simples'))
print('{:^46}'.format('NÃO coloca Parênteses'))
print('-'*46)
from time import sleep
from random import randint
num = randint(1,10)
sleep(1)
print('{:^46}'.format(f'O número Sorteado foi >>> {num}'))
print('-'*46)