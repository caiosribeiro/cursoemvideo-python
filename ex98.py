from time import sleep
def contador(i, f, p):
    print('-='*20)
    if p == 0:
        if i > f:
            p = -1
        elif f < i:
            p = 1
        print(f'Contagem de {i} até {f} de {p * (-1)} em {p * (-1)}')
        while i >= f:
            sleep(0.3)
            print(f'{i} ', end='')
            i += p
    elif p < 0:
        p *= (-1)
        print(f'Contagem de {i} até {f} de {p} em {p}')
        while i != f-p:
            sleep(0.3)
            print(f'{i} ', end='')
            i -= p
    elif i >= f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        while i >= f:
            sleep(0.3)
            print(f'{i} ', end='')
            i -= p
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        while i <= f:
            sleep(0.3)
            print(f'{i} ', end='')
            i += p
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
