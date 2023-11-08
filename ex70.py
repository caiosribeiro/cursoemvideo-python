print('-'*40)
print('          LOJA SUPER BARATÃO')
print('-'*40)
tot = 0
totacima = 0
prec = 0
cont = 0
prod = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    tot += preco
    cont += 1
    if preco > 1000:
        totacima += 1
    if cont == 1 or preco < prec:
        prec = preco
        prod = produto
    quest = ' '
    while quest not in 'SN':
        quest = str(input('Quer continuar? [S/N] ')).upper().strip()
    if quest == 'N':
        break
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {totacima} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prod} que custa R${prec:.2f}')
