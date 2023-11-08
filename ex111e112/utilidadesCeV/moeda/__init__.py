def dobro(n):
    r = n * 2
    return moeda(r)


def metade(n):
    r = n / 2
    return moeda(r)


def aumentar(x, y):
    r = x * y / 100 + x
    return moeda(r)


def diminuir(x, y):
    r = x - (x * y) / 100
    return moeda(r)


def moeda(n):
    return f'R${n:.0f},00'


def resumo(n=0, a=10, b=5):

    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'{a}% de aumento: \t{aumentar(n, a)}')
    print(f'{b}% de redução: \t{diminuir(n, b)}')
    print('-'*30)