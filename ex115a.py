from ex115b import *
arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

menu.cab()
n = op('\033[0;32mSua Opção: \033[m')
