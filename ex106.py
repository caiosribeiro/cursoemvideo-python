while True:
    print('\033[0;40;42m~'*30)
    print('   SISTEMA DE AJUDA PyHELP  ')
    print('~'*30)
    print('\033[m', end='')
    n = input('Função ou Biblioteca > ')
    if n.upper() == 'fim':
        print('\033[0;41m~'*12)
        print('  ATÉ LOGO!')
        print('~'*12)
        print('\033[m')
        break
    print('\033[0;44m~'*30)
    print(f"  Acessando o manual do chamado '{n}' ")
    print('~'*30)
    print('\033[m', end='')
    print('\033[7;40m')
    help({n})
    print('\033[m', end='')
