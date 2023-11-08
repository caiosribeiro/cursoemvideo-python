soma = total = 0
n = int(input('Digite o numero [999 para parar]: '))
while n != 999:
    n = int(input('Digite o numero [999 para parar]: '))
    total += 1
    if n != 999:
        soma += n
print('O total de numeros digitados foi: \033[1;33m{}\033[m'.format(total))
print('A soma de todos os números digitados é de: \033[1;33m{}\033[m'.format(soma))
