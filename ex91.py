from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jodagor4'] = randint(1, 6)
ranking = {}
print('Jogadores Sorteados:')
for j, n in jogadores.items():
    sleep(1)
    print(f'    O {j} tirou {n}')
print('-='*20)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)


