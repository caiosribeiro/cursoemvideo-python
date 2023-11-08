lista = []
lista1 = []
lista2 = []
lista3 = []
somapar = somaval = maior = v = 0
for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]: '))
    if c == 2:
        somaval += n
    if n % 2 == 0:
        somapar += n
    lista1.append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [1, {c}]: '))
    if c == 0:
        maior = n
    else:
        if n > maior:
            maior = n
    if c == 2:
        somaval += n
    if n % 2 == 0:
        somapar += n
    lista2.append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [2, {c}]: '))
    if c == 2:
        somaval += n
    if n % 2 == 0:
        somapar += n
    lista3.append(n)

lista.append(lista1[:])
lista1.clear()
lista.append(lista2[:])
lista2.clear()
lista.append((lista3[:]))
lista3.clear()
print('-='*30)
print(f'[  {lista[0][0]:^5}  ][  {lista[0][1]:^5}  ][  {lista[0][2]:^5}  ]'
      f'\n[  {lista[1][0]:^5}  ][  {lista[1][1]:^5}  ][  {lista[1][2]:^5}  ]'
      f'\n[  {lista[2][0]:^5}  ][  {lista[2][1]:^5}  ][  {lista[2][2]:^5}  ]')
print('-=' * 30)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somaval}.')
print(f'O maior valor da segunda linda é {maior}.')
print('-=' * 30)

