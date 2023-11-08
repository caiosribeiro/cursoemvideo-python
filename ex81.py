lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()
    if resp == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}', end='')
if 5 in lista:
    print(f'\nO valor 5 faz parte da lista na posição {lista.index(5)+1}')
if 5 not in lista:
    print('\nO valor 5 não se encontra.')