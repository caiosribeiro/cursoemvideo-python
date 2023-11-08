list = []
n_ant = pos = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > n_ant:
        list.append(n)
        print('Adicionado ao final da lista...')
        n_ant = n
    elif n < min(list):
        list.insert(0, n)
        print(f'Adicionado na posição 0 da lista...')
    elif n > min(list) and n < list[1]:
        list.insert(1, n)
        print(f'Adicionado na posição 1 da lista...')
    elif n > list[1] and n < list[2]:
        list.insert(2, n)
        print(f'Adicionado na posição 2 da lista')
    elif n < max(list) and n > list[pos]:
        list.insert(3, n)
        print(f'Adicionado na posição 4 da lista...')
    elif n < n_ant:
        list.insert(pos, n)
        print(f'Adicionado na posição {pos} da lista...')
        pos += 1
print(list)

'''
if c == 0 or n > list[-1]:
    lista.append(n)
    print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
'''
