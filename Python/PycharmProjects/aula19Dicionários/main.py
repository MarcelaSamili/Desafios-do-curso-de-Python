'''pessoas = {'nome': 'Marcela', 'idade': 20,  'sexo': 'F'}
print(pessoas['nome'])
print(pessoas['idade'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')# quando for assim tem quer ser aspas duplas pra nao da erro
pessoas['uf'] = 'MG'#para adicionar mais elementos ao dicionário
print(pessoas)
print(pessoas.values())#para pegar os valores
print(pessoas.keys())#para pegar as chaves
print(pessoas.items())#para pegar os valores e as chaves
for k, v in pessoas.items():#assim para pegar chave e valor
    print(f'O {k} é {v}')
for k in pessoas.keys():# assim ele vai pegar so as chaves
    print(f'{k}')
for v in pessoas.values():#assim ele vai pegar so os vlores
    print(f'{v}')
del pessoas['uf'] # assim ele vai apagar o elemento uf'''

#criando um dicionario detro de uma lista
'''brasil = []
estado1 = {'uf': 'Belo Horizonte', 'sigla': 'MG'}
estado2 = {'uf': 'Fortaleza', 'sigla': 'FO'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['uf'])
print(brasil[0]['sigla'])'''

#
estado = dict()
brasil = list()
for cc in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa:')).strip().title()
    estado['sigla'] = str(input('Sigla do estado:')).strip().upper()
    brasil.append(estado.copy())# o '[:]' nao funcina no dicionario entao para fazer uma cópia no dicionario se usa o copy
'''for e in brasil:
    print(e)
    for k, v in e.items():
        print(f'{k}: {v}:')'''
# ou
for e in brasil:
    for v in e.values():
        print(f'{v} ', end='')
    print()