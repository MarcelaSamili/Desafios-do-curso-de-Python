#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ['PEDRA','PALEL','TESOURA']
pc = randint(0,2)
print('''Suas opções:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador = int(input('Qual opção voce escolhe?'))
sleep(1)
print('JO!')
sleep(1)
print('KEM!')
sleep(1)
print('PÔ!!')
print('==='*10)
print('Computador jogou {}'.format(itens[pc]))#isso  "itens[pc]" é para poder pegar o numero e tranformar na palavra correspondente dentro de itens
print('Jogador jogou {}'.format(itens[jogador]))
print('==='*10)
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOADOR GANHOU!')
    elif jogador == 2:
        print('PC GANHOU!')
    else:
        print('OPÇÃO INVÁLIDA')
elif pc == 1:
    if jogador == 0:
        print('PC GANHOU!')
    elif jogador == 1:
         print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR GANHOU!')
    else:
        print('OPÇÃO INVÁLIDA')
elif pc == 2:
    if jogador == 0:
        print('JOGADOR GANHOU!')
    elif jogador == 1:
         print('PC GANHOU')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('OPÇÃO INVÁLIDA')
