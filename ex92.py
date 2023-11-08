from datetime import date
registro = {}
anoatual = date.today().year
while True:
    registro['nome'] = str(input('Nome: '))
    nasc = int(input('Ano de Nascimento: '))
    idade = anoatual - nasc
    registro['idade'] = idade
    registro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if registro['ctps'] == 0:
        break
    else:
        registro['contratação'] = int(input('Ano de contratação: '))
        registro['salário'] = float(input('Salário: R$ '))
        aposent = (anoatual - registro['contratação']) + 35 + idade
        registro['aposentadoria'] = aposent
    break
for k, v in registro.items():
    print(f'{k}: {v}')
