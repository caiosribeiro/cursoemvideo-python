print('Senquência de Fibonacci')
n = int(input('Digite um número: '))
print('Os primeiros \033[1;33m{}\033[m elementos de uma sequencia de Finobacci '.format(n))
f1 = 0
f2 = 1
n1 = 0
while n > n1:
    print('\033[1;33m{} →\033[m'.format(f1), end=' ')
    f3 = f1 + f2
    if f3 >= f2:
        f1 = f2
        f2 = f3
    n1 += 1
print('\033[1;31mFIM!\033[m')
