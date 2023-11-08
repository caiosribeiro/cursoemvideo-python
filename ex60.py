fat = int(input('Digite um número : '))
c = fat - 1
print('\033[1;34m{}!\033[m = {}'.format(fat, fat), end='')

while c != 0:
    fat = fat * c
    print('x{}'.format(c), end='')
    c -= 1
print(' = \033[1;33m{}\033[m'.format(fat))

'''n = fat -1
for c in range(fat, 1, -1):
    fat = fat * n
    print('x{}'.format(n), end='')
    n -= 1
print(' = \033[1;33m{}\033[m'.format(fat))'''

