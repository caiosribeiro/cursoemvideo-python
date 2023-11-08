c = 1
tabuada = 0
n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('=' * 30)
    for c in range(1,11,1):
        tabuada = n * c
        print(f'{n} X {c} = {tabuada}')
        c += 1
    print('=' * 30)
print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')



