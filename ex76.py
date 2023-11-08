listagem = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso',
            9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
p = 'LISTAGEM DE PREÇOS'
print('-'*43)
print(f'{p : ^40}')
print('-'*43)

for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<30} R$: {listagem[c+1]:>7.2f}.')
print('-'*43)
