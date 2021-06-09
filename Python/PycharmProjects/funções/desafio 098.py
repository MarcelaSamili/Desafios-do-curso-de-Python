#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:

from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('='*30)
    print(f'Contado de {i} ate {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.5)
            print(f' {cont}', end= ' ')
            cont += p
        print()

    else:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f' {cont}', end=' ')
            cont -= p
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('='*30)
print('Agora é a su vez!')
ini = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
contador(ini, fim, passo)
