from random import randint
from time import sleep
resposta = 'verdadeira'
computador = randint(0, 10)
cont = 1
(print('-=-' * 20))
print('Pense em um número entre 0 e 10, TENTE ADVINHAR!!')
(print('-=-' * 20))
while resposta != 'falsa':
    n = int(input('Em que número pensou? '))
    print('.....')
    sleep(1)
    if n == computador:
        print('Parabens você acertou!!')
        resposta = 'falsa'
    elif n > computador:
        print('Menos...')
        print('Que pena você errou :(')
        print('Digite novamente')
        cont += 1
    elif n < computador:
        print('Mais...')
        print('Que pena você errou :(')
        print('Digite novamente')
        cont += 1
print('Você tentou adivinhar {} vezes até acertar o número pensado "{}" '
      'do computador'.format(cont, computador))
