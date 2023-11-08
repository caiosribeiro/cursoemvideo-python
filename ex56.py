midade = 0
maior = 0
totalf = 0
nome1 = ''
for c in range(1, 5):
    print('---- {}ª PESSOA ----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    midade += idade
    if sexo in 'Ff' and idade < 20:
        totalf += 1
    if c == 1 and sexo in 'Mm':
        nome1 = nome
        maior = idade
    if sexo in 'Mm' and idade > maior:
        nome1 = nome
        maior = idade
print('A média de idade do grupo é de {} anos'.format(midade/4))
print('O homem mais velho se chama {} e tem {} anos'.format(nome1, maior))
print('Total de mulheres com menos de 20 anos é de: {}'.format(totalf))
