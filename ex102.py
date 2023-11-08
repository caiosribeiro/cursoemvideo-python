print('-'*30)
def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    if show == False:
        for c in range(n-1, 0, -1):
            n *= c-1
        return n
    if show == True:
        for c in range(n-1, 0, -1):
            n *= c
            print(f'{c+1} X ', end='')
        print('1 = ', end='')
        return n



print(fatorial(5,show=True))
help(fatorial)