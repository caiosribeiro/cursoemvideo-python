jogadores = []
jogador = {}
gols = []
tot = 0
while True:
    jogador.clear()
    gols.clear()
    print('-'* 20)
    jogador['nome'] = str(input('Nome do Jogador: '))
    quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for g in range(0, quant):
        gol = int(input(f'Quantos gols na partidas {g+1}? '))
        tot += gol
        gols.append(gol)
    jogador['gols'] = gols[:]
    jogador['total'] = tot
    jogadores.append(jogador.copy())
    while True:
        quest = str(input('Quer continuar? [S/N] ')).upper().strip()
        if quest in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if quest == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, j in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if n == 999:
        break
    if n >= len(jogadores):
        print(f'ERRO! Não existe jogar com código {n}!')
    else:
        print(f'-- LEVAMTAMENTO DO JOGADOR {jogadores[n]["nome"]}:')
        for j, g in enumerate(jogadores[n]['gols']):
            print(f'No jogo {j+1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')
