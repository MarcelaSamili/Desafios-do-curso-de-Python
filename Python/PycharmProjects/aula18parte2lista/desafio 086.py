#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
'''m = [[[], [], []], [[], [], []], [[], [], []]]
for c1 in range(0, 3):
    for c2 in range(0, 3):
        valor = int(input(f'Digite um valor para a posição |{c1},{c2}|:'))
        m[c1][c2].append(valor)
print('MATRIZ 3X3')
print(m[0][0], m[0][1], m[0][2])
print(m[1][0], m[1][1], m[1][2])
print(m[2][0], m[2][1], m[2][2])'''

#jeito da aula
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range( 0, 3):
        m[linha][coluna] = int(input(f'Digite um valor para a posição [{linha},{coluna}]:'))
print('{:=^19}'.format("MATRIZ 3X3"))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{m[linha][coluna]:^4}]', end='')
    print()