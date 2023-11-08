def leiaDinheiro(p):
    while True:
        resp = str(input(p)).replace(',', '.').strip()
        if resp.isalpha() or resp == '':
            print(f'\033[0;31mERRO: "{resp}" é um preço inválido!\033[m')
        else:
            break
    return float(resp)