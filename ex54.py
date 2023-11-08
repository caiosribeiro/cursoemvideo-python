from _datetime import datetime

x = datetime.now()
y = int(x.strftime("%Y"))
s = 0
t = 0
m = y - 18
for c in range(1, 8):
    n = int(input('ano de nascimento: '))
    if n <= m:
        s += 1
    else:
        t += 1
print('O total de maiores de idade é: {}'.format(s))
print('O total de menores é: {}'.format(t))
