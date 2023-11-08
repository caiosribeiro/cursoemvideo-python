galera = []
pessoas = {}
idtot = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    galera.append(pessoas.copy())
    idtot += pessoas['idade']
    while True:
        quest = str(input('Quer continuar? [S/N]')).upper()[0]
        if quest in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if quest == 'N':
        break
idmedia = idtot / len(galera)
print(f'- O grupo tem {len(galera)} pessoas.')
print(f'- A média de idade é de {idmedia:.1f}')
print(f'- As mulheres cadastradas foram: ', end='')
for m in galera:
    if m['sexo'] in 'Ff':
        print(f'{m["nome"]} ', end='')
print()
print('- Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] > idmedia:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>')