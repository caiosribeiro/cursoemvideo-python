times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
          'Bragantino', 'Athletico-PR', 'Internacional', 'Fluminense',
         'América-MG', 'Atlético-GO', 'Cuiabá', 'Ceará SC', 'São Paulo',
         'Juventude', 'Santos', 'Grêmio', 'Bahia', 'Sport Recife',
         'Chapecoense')
print(f'Lista de times do brasileirão: {times}')
print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
for pos, times in enumerate(times):
    if times == 'Chapecoense':
        print(f'A {times} está na {pos+1}º posição')