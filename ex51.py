p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + (10 - 1) * r
print('Os 10 primeiro termos da progressão são:')
for c in range(p, d + r, r):
    print(c, end=' ')

