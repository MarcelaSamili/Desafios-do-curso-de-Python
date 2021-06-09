#Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
num = list()
for c in range(0, 5):
    val = int(input('Digite um número:'))
    if c == 0 or val > num[-1]:
        num.append(val)
        print('Adicionado no fim da lista...')
    else:
        pos = 0
        while pos < len(num):
            if val <= num[pos]:
                num.insert(pos, val)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores adicionados foram {num}')















