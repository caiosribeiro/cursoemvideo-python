from random import randint
sorte = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os 5 números sorteados foram: ', end='')
for c in range(0, len(sorte)):
    print(f'{sorte[c]}', end=' ')
print(f'\nO maior número é: {max(sorte)}')
print(f'O menor número é: {min(sorte)}')





