#: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
from time import sleep
print('---'*15)
print('{: ^40}'.format('LOJA VOLTE SEMPRE'))
print('---'*15)
totcompra = maisde1000 = cont = maisbarato = 0
pmb = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço R$'))
    cont += 1
    totcompra += preco
    if preco > 1000:
        maisde1000 += 1
    if cont == 1:
        maisbarato = preco
        pmb = produto
    else:
        if preco < maisbarato:
            maisbarato = preco
            pmb = produto
    compra = ' '
    while compra not in 'SN':
        compra = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if compra == 'S':
        print('PROXIMA COMPRA')
    elif compra == 'N':
        break
print('Finalizando compra...')
sleep(1)
print('{:-^40}'.format('Compra finalizada!'))
print(f'O total da compra foi de: R${totcompra}')
print(f'Temos {maisde1000} produto/s custando mais de R$1000.')
print(f'O produto mais barato foi {pmb} que custa {maisbarato}')
