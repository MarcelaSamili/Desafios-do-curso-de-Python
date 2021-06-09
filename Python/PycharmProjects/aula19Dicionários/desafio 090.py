dicionario = dict()
dicionario['aluno(a)'] = str(input('Nome:')).strip().title()
dicionario['media'] = float(input('Média:'))

if dicionario['media'] < 5:
    dicionario['situação'] = 'Repovado!'
else:
    if dicionario['media'] >= 5:
        dicionario['situação'] = 'Aprovado!'


for k, v in dicionario.items():
    print(f'{k} : {v}')