
def notas(* n, sit=False):
    """
     -> notas serve para analizar notas e situação de alunos
    :param n: uma ou mais notas dos alunos
    :param sit:opicional para ver a situação
    :return:dicionario com varias informaçoes sobre a situaçao da turma
    """
    d = {}
    d['Quantidade de notas'] = len(n)
    d['Maior nota '] = max(n)
    d['Menor nota'] = min(n)
    d['Media'] = sum(n) / len(n)
    if sit == True:# se quiser nao precisa por o == True, funciona do mesmo jeito
        if d['Media'] > 5.0:
            d['Situação'] = 'Ótima'
        elif d['Media'] == 5.0:
            d['Situação'] = 'Média'
        else:
            d['Situação'] = 'Ruim'
    return d

resp = notas(5, 8, 10, sit=True)
print(resp)
