#crie um programa que leia o comprmento de tres retas e diga se elas podem ou não formar um triangulo
a = float(input('Quanto mede o primeiro lado:'))
b = float(input('Quanto mede o segundo lado:'))
c = float(input('Quanto mede o terceliro lado:'))
if a + b > c > a - b and a + c > b > a - c or c + b > a > c - b:
    print('Essas retas \033[32mFORMAM\033[m um triangulo')
else:
    print('Essas retas \033[31mNAO formam\033[m um triangulo')