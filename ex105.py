def notas(* n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação do aluno
    '''
    soma = 0
    aluno = {}
    aluno['total'] = len(n)
    aluno['Maior'] = max(n)
    aluno['Menor'] = min(n)
    for c in n:
        soma += c
    aluno['Média'] = soma / len(n)
    if sit == True:
        if aluno['Média'] >= 7:
            aluno['Situação'] = 'BOA'
        if 5.5 <= aluno['Média'] < 7:
            aluno['Situação'] = 'RAZOÁVEL'
        if aluno['Média'] < 5.5:
            aluno['Situação'] = 'RUIM'
    return aluno


resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)
