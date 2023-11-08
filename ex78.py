list = []
for c in range(0, 5):
    list.append(int(input('Digite um valor: ')))
print('=-' * 30)
maior = max(list)
menor = min(list)
print(f'Você digitou os valores {list}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, maior in enumerate(list):
    if maior == max(list):
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for p, menor in enumerate(list):
    if menor == min(list):
        print(f'{p}... ', end='')
