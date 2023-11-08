from random import randint
from time import sleep
lista = []
jogos = []
tot = 1
print('-'*40)
p = 'JOGO NA MEGA SENA'
print(f'{p:^40}')
print('-'*40)
n = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(2)
print('\n-=-=-=-= < BOA SORTE! > -=-=-=-')
