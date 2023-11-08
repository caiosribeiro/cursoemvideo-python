n = int(input('Digite um número: '))
print('A tabuada de {} é:'.format(n))
for c in range(1, 11):
    print('{} X  {:2} = {}' .format(n, c, n*c))
