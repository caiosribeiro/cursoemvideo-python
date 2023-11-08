from time import sleep


def maior(* v):
    print("-=" * 30)
    print('Analisando os valores passados...')
    if v != ():
        for n in v:
            sleep(0.3)
            print(f'{n}', end=' ')
        print(f'Foram informados {len(v)} valores ao todo.')
        print(f'O maior valor informado foi {max(v)}')
    else:
        print(f'Foram informados 0 valores ao todo.')
        print(f'O maior valor informado foi 0')
    sleep(0.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
