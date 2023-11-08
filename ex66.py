quant = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'A soma dos \033[1;33m{quant}\033[m valor foi \033[1;33m{soma}\033[m!')
