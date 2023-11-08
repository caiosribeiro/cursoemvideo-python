p = int(input(('Digite o primeiro termo: ')))
r = int(input('Digite a razão: '))
c = 1
print('Os 10 primeiro termos da progressão são:')
print('\033[1;33m10\033[m', end=' ')
while c != 10:
    p = p + r
    print('\033[1;33m{}\033[m'.format(p), end=' ')
    c += 1

