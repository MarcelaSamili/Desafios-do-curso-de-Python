#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cadastro = {}
dados = []
soma_idade = 0

while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome:')).strip().title()
    cadastro['sexo'] = str(input('Sexo:[F/M]')).strip().upper()[0]
    while cadastro['sexo'] not in 'FM':
            print('Erro! somente F ou M.')
            cadastro['sexo'] = str(input('Sexo:[F/M]')).strip().upper()[0]
            if cadastro['sexo'] in 'FM':
                break
    cadastro['idade'] = int(input('Idade:'))

    dados.append(cadastro.copy())

    soma_idade += cadastro['idade']



    while True:
        cond = str(input('Quer continuar?[S/N]:')).strip().upper()[0]
        if cond in 'SN':
            break
        print('ERRO! S ou N para resposta')
    if cond == 'N':
        break


print(f'  A)  O numero de pessoas cadastradas foi de: {len(dados)} pessoas')
media_idade = soma_idade / len(dados)
print(f'  B)  A média de idade é de: {media_idade:.2f}')
print(f'  C)  A mulheres cadastradas foram:', end=' ')

for p in dados:
    if p["sexo"] == 'F':
        print(f'{p["nome"]},', end=' ')
print()
print(f'  D)  As pessoas que estão acima da média são:', end=' ')
for p in dados:
    if p["idade"] >= media_idade:
        print('     ')
        for k, v in p.items():
            print(f'        {k} = {v}', end=' ')



