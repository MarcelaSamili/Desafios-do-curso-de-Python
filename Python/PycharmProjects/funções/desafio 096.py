# Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(l, c):
    a = l * c
    print(f'A area de um terreno de {l} X {c} é de {a:.2f} m²')

larg = float(input('LARGURA(m²):'))
comp = float(input('COMPRIMENTO(m²):'))
area(larg, comp)