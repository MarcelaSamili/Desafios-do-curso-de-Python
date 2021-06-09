#crie um programa que leia um numero qualquer na tela e mostre na tela sua porção inteira.
from math import trunc
n = float(input('Digite um número:'))
print('A porção inteira do número {} é {}.'.format(n, trunc(n)))

'''n = float(input('Digite um valor:'))
print('A porção inteira de {} é {}.'.format(n, int(n)))'''
