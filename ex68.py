from random import randint
print('=-'*20)
print('         VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
soma = 0
vit = 0
while True:
    n = int(input('Diga um valor: '))
    pc = randint(0,10)
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-'*40)
    soma = pc + n
    print(f'Você jogou {n} e o computador {pc}. Total de {soma} ',end='')
    if pi in 'Pp':
        if soma % 2 == 0:
            print('DEU PAR')
            print('Você VENCEU!\nVamos jogar novamente...')
            vit += 1
        if soma % 2 != 0:
            print('DEU IMPAR')
            print('Você PERDEU!')
            break
    if pi in 'Ii':
        if soma % 2 != 0:
            print('DEU ÍMPAR')
            print('Você VENCEU!\nVamos jogar novamente...')
            vit += 1
        if soma % 2 == 0:
            print('DEU PAR')
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {vit} vezes.')
