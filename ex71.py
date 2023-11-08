print('='*40)
print('             BANCO DO CEV')
print('='*40)
totcinq = totvin = totdez = totum = 0
cinq = 50
vin = 20
dez = 10
um = 1
valor = int(input('Que valor você quer sacar? R$'))
total = valor
while True:
    total = total - cinq
    totcinq += 1
    if total < 50:
        break
if total < 50 and total >= 20:
    while True:
        total = total - vin
        totvin += 1
        if total < 20:
            break
if total < 20 and total >= 10:
    while True:
        total = total - dez
        totdez += 1
        if total < 10:
            break
if total < 10 and total >= 1:
    while True:
        total = total - um
        totum += 1
        if total < 1:
            break
if totcinq > 0:
    print(f'Total de {totcinq} cédulas de R${cinq}')
if totvin > 0:
    print(f'Total de {totvin} cédulas de R${vin}')
if totdez > 0:
    print(f'Total de {totdez} cédulas de R${dez}')
if totum > 0:
    print(f'Total de {totum} cédulas de R${um}')
print('\033[1;31mCONSEGUI PORRA ADEUS\033[m')
