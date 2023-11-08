lista = []
lista_par = []
lista_imp = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print(f'A lista completa é {lista}')
for v in lista:
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_imp.append(v)
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_imp}')