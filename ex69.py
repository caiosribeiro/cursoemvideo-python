print('==========FIM DO PROGRAMA==========')
totid = 0
tothom = 0
totmum = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')
    print('-' * 25)
    idad = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F] ')).upper().strip()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idad > 18:
        totid += 1
    if sex == 'M':
        tothom += 1
    if sex == 'F' and idad < 20:
        totmum += 1
    if resp == 'N':
        break
print('========= FIM DO PROGRAMA ==========')
print(f'Total de pessoas com mais de 18 anos: {totid}')
print(f'Ao todo temos {tothom} homens cadastrados')
print(f'E temos {totmum} mulheres com menos de 20 anos')
