from datetime import date
print('-'*30)
ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - ano


def voto(n):
    '''
    atual = date.today().year
    idade = atual - n
    print(f'Com {idade} anos:', end=' ')
    '''
    if idade < 18:
        return "NÃO VOTA."
    elif 18 <= idade < 65:
        return "VOTO OBRIGATÓRIO."
    elif idade >= 65 or 16 >= idade < 18:
        return "VOTO OPCIONAL."


resp = voto(ano)
'print(f"{resp}")'
print(f'Com {idade} anos: {resp}')

