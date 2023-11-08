n = int(input('Digite um número: '))
resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
quant = 1
soma = 0 + n
maior = menor = 0
while resp == 'S':
    n = int(input('Digite um número: '))
    quant += 1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < maior:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('Foram digitados \033[1m{}\033[m números'.format(quant))
print('A \033[4mmédia\033[m: \033[1;33m{}\033[m'.format(soma/quant))
print('O \033[4mmaior\033[m número: \033[1;33m{}\033[m'.format(maior))
print('M \033[4mmenor\033[m número: \033[1;33m{}\033[m'.format(menor))





