print('-'*46)
print('{:^46}'.format('Contando Vogais com TUPLA'))
print('-'*46)
palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso',
            'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado',
            'Programador', 'Futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end=' ')
    for letras in p:
        if letras.lower() in 'aàáãâeèéêîòóOòõu':
            print(letras,end=' ')
print('\n','-'*46)