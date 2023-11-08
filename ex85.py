numeros = []
pares = []
impares = []
for c in range(0, 7):
    n = int(input('1ºNúmero: '))
    if n % 2 == 0:
        pares.append(n)

    if n % 2 == 1:
        impares.append(n)
pares.sort()
numeros.append(pares[:])
pares.clear()
impares.sort()
numeros.append(impares[:])
impares.clear()
print('-='*30)
print(f'Os valor digitados foram:{numeros[0]}')
print(f'Os valor ímpares digitador foram: {numeros[1]}')

