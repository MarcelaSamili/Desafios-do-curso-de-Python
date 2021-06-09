# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:5! = 5 x 4 x 3 x 2 x 1 = 120
'''import math
v = int(input('Digite um número:'))
fatorial = math.factorial(v)
print('O fatorial do número {} é {}'.format(v, fatorial))'''
n = int(input('Digite um número:'))
c = n
f = 1
print('Calculando {}! = '.format(n),end= ' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end= ' ')
    f *= c
    c -= 1
print('{}'.format(f))
'''n = int(input('Digite um número:'))
c = n
f = 1
print('Calculando {}! = '.format(c), end=' ')
for c in range(c, 0, -1):
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
print('{}'.format(f))'''
