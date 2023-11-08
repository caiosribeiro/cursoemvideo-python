def leiaint(resp):
    while True:
        r = input(resp)
        if r.isnumeric():
            break
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
    return r


# Program Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
