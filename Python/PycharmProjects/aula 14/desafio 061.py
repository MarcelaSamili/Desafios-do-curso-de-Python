#  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.
p = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a rasão dessa PA:'))
termo = p
cont = 1
while cont <= 10:
    print('{} - '.format(termo),end=' ')
    termo += r
    cont += 1
print('FIM')


