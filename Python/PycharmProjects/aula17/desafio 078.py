#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista.
num = []
c = maior = menor = 0
for n in range(0, 4):
    num.append(int(input(f'Digite um número na posição {n}:')))
    if n == 0:
        maior = menor = num[n]
    else:
        if num[n] > maior:
            maior = num[n]
        if n < menor:
            menor = num[n]
print(f'O MAIOR número foi {maior} nas posiçoes ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='' )
print()
print(f'O MENOR número foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
#outro jeito
'''num = []
for n in range(0, 4):
    num.append(int(input(f'Digite um número na posição {n}:')))
print(f'O MAIOR número foi {max(num)} nas posiçoes ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}...', end='' )
print()
print(f'O MENOR número foi {min(num)} nas posições ', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}...', end='')'''


