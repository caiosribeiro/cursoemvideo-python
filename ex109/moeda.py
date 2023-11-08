def moeda(n):
    return f'R${n:.0f},00'

def dobro(n, show=False):
    if show == True:
        return moeda(n)
    else:
        return n * 2


def metade(n, show=False):
    r = n / 2
    if show == True:
        return moeda(n)
    else:
        return r


def aumentar(x, y, show=False):
    n = (x * y) / 100
    if show == True:
        return moeda(n)
    else:
        return n + x


def diminuir(x, y, show=False):
    n = (x * y) / 100
    if show == True:
        return moeda(n)
    else:
        return x - n



