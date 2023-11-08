s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        cont += 1
        s += n
print('A soma de todos os {} números pares digitados é: {}'.format(cont, s))
