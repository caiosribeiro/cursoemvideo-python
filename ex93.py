jogador = {}
gols = []
tot = 0
jogador['nome'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for g in range(0, quant):
    gol = int(input(f'Quantos gols na partidas {g+1}? '))
    tot += gol
    gols.append(gol)
jogador['gols'] = gols[:]
jogador['total'] = tot
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {quant} partidadas.')
for p, g in enumerate(gols):
    print(f'    => Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {tot} gols.')
