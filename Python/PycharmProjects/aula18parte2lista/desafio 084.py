pessoas = []
dados = []
maior = 0
menor = 0
while True:
    dados.append(str(input('Nome:')).strip().title())
    dados.append(int(input('Peso:')))

    if len(pessoas) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    cond = ' '
    if cond not in 'SN':
        cond = str(input('Quer contnuar?[S/N]')).strip().upper()[0]
        if cond == 'N':
            break

print('==='*14)
print(f'Tiveram {len(pessoas)} pessoa cadastradas')
print(f'Os mais pesados da lista são:', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}...', end=' ')
print('!')
print(f'Os mais leves da lita são:', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}...', end=' ')
print('!')






