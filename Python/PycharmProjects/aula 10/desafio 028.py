#faça um programa que faça o pc pençar em um numero inteiro de 0 a 5 e peça pra o usuario adivinhar qual o pc vai esolher
#o programa deverá ecrever na tela se o usuario venceu ou perdeu
'''import random
print('==='*22)
print('Vou escolher um numero de 0 a 5, tente adivinhar qual eu escolhi')
print('==='*22)
n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = [n0,n1,n3,n4,n5]
escolhido = random.choice(lista)
pergunta = int(input('Qual eu escolhi?'))
if pergunta == escolhido:
    print('Voce ganhou!!! pois eu ecolhi o número {}'.format(escolhido))
else:
    print('HAHA EU GANHEI!!! pois eu escolhi o {}'.format(escolhido))'''
#resolução da aula
from random import randint
from time import sleep
computador = randint(0, 5)
print('---'*15)
print('\033[33mAdivinha qual número estou pensado de 0 a 5\033[m')
print('---'*15)
jogador = int(input('Em qual número eu pensei ?'))
print('PROCESSANDO...')
sleep(1.5)
if computador == jogador:
    print('\033[1;34;43mVOCÊ GANHOU!!!\033[m eu escolhi o número \033[34m{}'.format(computador))
else:
    print('\033[1;30;45mEU GANHEI!!\033[m pois escolhi o número \033[34m{}'.format(computador))


