#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = 0
soma_tcol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        m[linha][coluna] = int(input(f'Digite um valor para a posição [{linha},{coluna}]:'))

        if m[linha][coluna] % 2 == 0:
            somap += m[linha][coluna]

        soma_tcol += m[linha][2]

print('{:=^19}'.format("MATRIZ 3X3"))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{m[linha][coluna]:^4}]', end='')
    print()
print('==='*5)
print(f'A soma de todos os números pares é: {somap}')
print(f'A soma da terceira coluna é de: {soma_tcol}')
print(f'O maior valor da segunda linha é: ', end='')

for p in m[1]:
    if p == max(m[1]):
        print(f'{p}', end='')



