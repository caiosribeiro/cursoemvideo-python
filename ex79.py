list = []
while True:
    n = int(input('Digite um valor: '))
    if n not in list:
        list.append(n)
        print('Valor adicionado com sucesso...')
    elif n in list:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
list.sort()
print('Você digitou os valores: ', end='')
for c in list:
    print(f'{c}', end=' ')
