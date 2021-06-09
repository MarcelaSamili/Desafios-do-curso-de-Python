#Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci
print('***'*10)
print('FREQUENCIA DE FIBRONACCI')
print('***'*10)
n = int(input('Voce quer quantos termos:'))
t1 = 0
t2 = 1
print('{} - {} -'.format(t1, t2), end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{} -'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
