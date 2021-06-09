#Desenvolva um programa que leia um numero inteiro qualquer e dê a sua tabuada
#com variavel
'''n = float(input('Me diga um número, e eu te dou a tabuada:'))
m0 = n*0
m1 = n*1
m2 = n*2
m3 = n*3
m4 = n*4
m5 = n*5
m6 = n*6
m7 = n*7
m8 = n*8
m9 = n*9
m10 = n*10
print('A tabuada do número {} é: \n{} x 0 = {}\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {} \n{} x 9 = {}\n{} x 10 = {}.'.format(n, n, m0, n, m1, n, m2, n, m3, n, m4, n, m5, n, m6, n, m7, n, m8, n, m9, n, m10))'''
#sem variavel
n = float(input('Me diga um número, e eu te dou a tabuada:'))
print( '-' * 15)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('-'*15)
