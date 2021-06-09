print('Digite quatro valores.')
n = int(input('Primero valor:')), int(input('Segundo valor:')), int(input('Terceiro valor:')), int(input('Quarto valor:'))
print(f'Os valores digitados foram:{n}')
print(f'O numero 9 apareeus {n.count(9)} vezes')
if 3 in n:
    print(f'O numero 3 apareceu na {n.index(3)+1}° posicao')
else:
    print('Nao ha o número 3  na lista')
print('Os valores pares são:', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')


