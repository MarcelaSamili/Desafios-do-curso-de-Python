#crie um programa que leia um numero inteiro qualquer e mostre na tela se ele é par o ípar
n = int(input('Digite um núnmero:'))
r = n % 2
if r == 0:
    print('Esse número é PAR')
else:
    print('Esse numero é ÍMPAR')
#Esse modo  da certo porque TODO numero PAR dividido por 2 tem o resto da divisao = 0 e todo numero IMPAR tem resto = 1
