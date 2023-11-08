def ficha(n, g):
    if n == '':
        n = '<desconhecido>'
    if g == '' or g != int:
        g = 0
    print(f'O Jogador {n} fez {g} gol(s) no campeonato')


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
ficha(nome, gols)
