#Faça um programa que leia o comprimeno do cateto oposto e do cateto adjacente de um triangulo retangulo
# e mostre o comprimento da hipotenusa.a²+b2=raizc²
#modo direto
'''from math import hypot
co = float(input('Digite o carteto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
print('A hipotenusa é {:.2f}'.format(hypot(co,ca)))'''
#modo indireto
import math
co = float(input('Digite o carteto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
h = math.hypot(co,ca)
print('A hipotenusa é {:.2f}'.format(h))
#matematico
'''from math import pow
co = float(input('Digite o carteto oposto:'))
ca = float(input(('Digite o cateto adjacente:')))
h = co**2 + ca**2 # ** (1/2)
print('A hipotenusa é {:.2f}'.format(pow(h, (1/2))))'''

