print('=-='*16)
print('{:^16}'.format('Exemplos de Tuplas - Variáveis Compostas'))
print('=-='*16,'\n')

 # TUPLAS COM PARÊNTESES ():
lanche = ('Hamburguer','Suco', 'Pizza','Pudim')
print(lanche)
# print >>> ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

# TUPLAS SEM PARÊNTESES ():
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche)
# print >>> ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#============================================================================

lanche = ('Hamburguer','Suco', 'Pizza','Pudim')
print(lanche [1])
# print >>> Suco

lanche = ('Hamburguer','Suco', 'Pizza','Pudim')
print(lanche [3])
# print >>> Pudim

lanche = ('Hamburguer','Suco', 'Pizza','Pudim')
print(lanche [-2])
# print >>> Pizza

lanche = ('Hamburguer','Suco', 'Pizza','Pudim')
print(lanche [1:3])
# print >>> ('Suco', 'Pizza')

lanche = ('Hamburguer','Suco', 'Pizza','Pudim')
print(lanche [2:])
# print >>> ('Pizza', 'Pudim')

lanche = ('Hamburguer','Suco', 'Pizza','Pudim')
print(lanche [:2])
# print >>> ('Hamburguer', 'Suco')

lanche = ('Hamburguer','Suco', 'Pizza','Pudim')
print(lanche [-2:])
# print >>> ('Pizza', 'Pudim')

lanche = ('Hamburguer','Suco', 'Pizza','Pudim')
print(lanche [-3])
# print >>> Suco

lanche = ('Hamburguer','Suco', 'Pizza','Pudim')
print(lanche [-3:])
# print >>> ('Suco', 'Pizza', 'Pudim')
