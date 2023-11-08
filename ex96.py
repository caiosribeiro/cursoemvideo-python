def area(l, c):
    print('Controle de Terrenos')
    print('-'*20)
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    t = l * c
    print(f'A área de um terreno {l}x{c} é de {t:.1f}m²')


area(1, 1)
