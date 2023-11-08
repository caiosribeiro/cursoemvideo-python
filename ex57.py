c = 'S'
while c != 'N':
    sexo = str(input('Digite o sexo: ')).upper().strip()[0]
    if sexo != 'F' and sexo != 'M':
        print('O dígito foi "{}"'.format(sexo))
        print('Digito inválido, digite novamente!')
    else:
        print('O dígito foi "{}"'.format(sexo))
        if sexo == 'M':
            print('O sexo da pessoa é MASCULINO')
        else:
            print('o sexo da pessoa é FEMININO')
        c = 'N'



