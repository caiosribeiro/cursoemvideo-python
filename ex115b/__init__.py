from ex115b import menu
from time import sleep
from ex104 import leiaint


arq = 'cursoemvideo.txt'
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print('-'*30)
        print('PESSOAS CADASTRADAS'.center(30))
        print('-'*30)
        for linha in a:
            dado = linha.strip(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]}{dado[1]}')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na arbetura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
        finally:
            a.close()


def op(msg):
    while True:
        try:
            while True:
                r = int(input(msg))
                if 0 < r < 4:
                    if r == 1:
                        lerArquivo(arq)
                        sleep(1.5)
                        menu.cab()
                    elif r == 2:
                        print('-' * 30)
                        print('NOVO CADASTRO'.center(30))
                        nome = str(input('Nome: '))
                        idade = leiaint('Idade: ')
                        cadastrar(arq, nome, idade)
                        print('-' * 30)
                        sleep(1.5)
                        menu.cab()
                    elif r == 3:
                        sleep(1)
                        print('-' * 30)
                        print('Saindo do sitema... Até logo!'.center(30))
                        print('-' * 30)
                        break
                else:
                    print('\033[0;31mERRO: Digite uma opção válida!\033[m')
                    sleep(1.5)
            return r

        except:
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
