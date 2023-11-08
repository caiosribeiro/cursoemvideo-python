lista = []
list1 = []
list2 = []
list3 = []
for c in range(0, 3):
    list1.append(int(input(f'Digite um valor para [0, {c}]: ')))

for c in range(0, 3):
    list2.append(int(input(f'Digite um valor para [1, {c}]: ')))

for c in range(0, 3):
    list3.append((int(input(f'Digite um valor para [2, {c}]: '))))
lista.append(list1[:])
list1.clear()
lista.append(list2[:])
list2.clear()
lista.append(list3[:])
list3.clear()
print('-='*30)
print(f'[  {lista[0][0]:^5}  ][  {lista[0][1]:^5}  ][  {lista[0][2]:^5}  ]'
      f'\n[  {lista[1][0]:^5}  ][  {lista[1][1]:^5}  ][  {lista[1][2]:^5}  ]'
      f'\n[  {lista[2][0]:^5}  ][  {lista[2][1]:^5}  ][  {lista[2][2]:^5}  ]')

'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ))'
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()
'''