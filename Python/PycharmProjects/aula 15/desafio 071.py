# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('---'*15)
print('{: ^40}'.format('SEU BANCO'))
print('---'*15)
valor = int(input('Quanto voce quer sacar: R$'))
total = valor
ced = 50
totc = 0
while True:
    if total >= ced:
        total -= ced
        totc += 1
    else:
        if totc > 0:
            print(f'Deu {totc} cedulas de R${ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totc = 0
        if total == 0:
            break
print('Volte sempre!')
#tenta refazer esse pq voce não coseguiu


