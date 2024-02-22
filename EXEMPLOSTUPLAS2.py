print('=-='*16)
print('{:^16}'.format('Exemplos de Tuplas  2 - Variáveis Compostas'))
print('=-='*16,'\n')
# TUPLAS SÃO IMUTÁVEIS >>> Não pode fazer mudanças

lanche = 'hamburguer', 'Suco', 'Pizza','Pudim'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('='*36)
#==========================================================================

lanche = 'hamburguer', 'Suco', 'Pizza','Pudim'
print(len(lanche))
print('Comi pra caramba!')
print('='*36)
#==========================================================================

lanche = 'hamburguer', 'Suco', 'Pizza','Pudim','Batata Frita'
print(len(lanche))
print('Comi pra caramba!')
print('='*36)
#==========================================================================

lanche = 'hamburguer', 'Suco', 'Pizza','Pudim','Batata Frita'
for cont in range (0,len(lanche)):
    print(cont)
print('Comi pra caramba!')
print('='*36)
#==========================================================================

lanche = 'hamburguer', 'Suco', 'Pizza','Pudim','Batata Frita'
for cont in range (0,len(lanche)):
    print(lanche[cont])
print('Comi pra caramba!')
print('='*36)

#==========================================================================
# EXEMPLOS DE TUPLAS QUE TRAZEM O MESMO RESULTADO

# EXEMPLO 1
lanche = 'hamburguer', 'Suco', 'Pizza','Pudim','Batata Frita'
for cont in range (0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')
print('-'*36)

# EXEMPLO 2
lanche = 'hamburguer', 'Suco', 'Pizza','Pudim','Batata Frita'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('-'*36)

# EXEMPLOS QUE NECESSITAM DE POSIÇÃO
# EXEMPLO 3
lanche = 'hamburguer', 'Suco', 'Pizza','Pudim','Batata Frita'
for cont in range (0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')
print('-'*36)

# EXEMPLO 4 >> Com ENUMERATE
for pos, COMIDA in enumerate (lanche):
    print(f'Eu vou comer {lanche[cont]} na posição {pos}')
print('Comi pra caramba!')
print('='*36)
#========================================================================
# EXEMPLO COM SORTED >>> ORGANIZADO EM ORDEM ALFABETICA

lanche = 'hamburguer', 'Suco', 'Pizza','Pudim','Batata Frita'
print(sorted(lanche))

#==========================================================================
print('='*36)
