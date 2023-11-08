from random import randint
from time import sleep
numeros = []


def sorteia(n):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        n = randint(1, 10)
        numeros.append(n)
        sleep(0.3)
        print(n, end=' ')
    print('PRONTO!')


def somaPar(p):
    soma = 0
    sorteia(numeros)
    print(f'Somando os valores pares de {numeros}, temos ', end='')
    for p in numeros:
        if p % 2 == 0:
            soma += p
    print(soma)


somaPar(numeros)
