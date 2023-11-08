numeros = (int(input('Digite um número: ')),
            int(input('Digite outro número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite o último número: ')))
if 9 in numeros:
    print(f'O número 9 apareceu {numeros.count(9)} vez')
else:
    print('O número 9 não apareceu nenhuma vez')
if 3 in numeros:
    print(f'O número 3 apareceu em {numeros.index(3)+1}º posição')
else:
    print('O número 3 não apareceu em nenhuma posição')
print('Os números pares são: ', end='')
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=' ')
