p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
cont = 1
print('\033[1;33m{}\033[m'.format(p), end=' ')
while c < 10:
    p = p + r
    cont += 1
    c += 1
    print('\033[1;33m{}\033[m'.format(p), end=' ')
c1 = 0
resp = 1
while resp != 0:
    resp = int(input('\nVocê quer mostrar mais quantos termos? '))
    resp1 = resp - resp
    while resp1 < resp:
        p = p + r
        cont += 1
        resp1 += 1
        print('\033[1;34m{}\033[m'.format(p), end=' ')
print('\nForam mostrados {} termos no total'.format(cont))
print('\nFIM')
