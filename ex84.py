pessoas = []
inserir = []
totpessoas = maior = menor = c = 0
while c > -1:
    nome = (str(input('Nome: ')))
    peso = (float(input('Peso: ')))
    if c == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    inserir.append(nome)
    inserir.append(peso)
    pessoas.append(inserir[:])
    inserir.clear()
    totpessoas += 1
    c += 1
    quest = ' '
    while quest not in 'SN':
        quest = str(input('Quer continuar? [S/N]')).upper().strip()
    if quest == 'N':
        break
print(f'Ao todo, você cadastrou {totpessoas} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for c in pessoas:
    if c[1] == maior:
        print(f'{c[0]}, ', end='')
print(f'\nO menor peso foi de {menor:.1f}Kg. Peso de ',end='')
for c in pessoas:
    if c[1] == menor:
        print(f'{c[0]}, ', end='')
