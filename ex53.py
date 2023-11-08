f = str(input('Digite uma frasa: ')).replace(" ", "")
i = f[::-1]
print('{}'.format(i))
if f == i:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')
