#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
print('VAMOS JOGAR JOKEMPO!')
print('''Coloque: 
[1]PEDRA
[2]PAPEL
[3]TESOURA''')
op = input('Qual opção voce escolhe?')
lista = ['1','2','3']
pc = random.choice(lista)
sleep(1)
print('\033[36mJO!')
sleep(1)
print('\033[36mKEM!')
sleep(1)
print('\033[36mPO!!\033[m')
if op == pc or pc == op:
    print('\033[34mEMPATE!\033[m, PC TAMBÉM ESCOLHEU {} '.format(pc))
elif op == '1' and pc == '2':
    print('\033[33mPC GANHOU!\033[m, PC ESCOLHEU {} '.format(pc))
elif op == '2' and pc == '1':
    print('\033[32mJOGADOR GANHOU!\033[m, PC ESCOLHEU {}'.format(pc))
elif op == '2' and pc == '3':
    print('\033[33mPC GANHOU!\033[m, PC ESCOLHEU {}'.format(pc))
elif op == '3' and pc == '2':
    print('\033[32mJOGADOR GANHOU!\033[m, PC ESCOLHEU {}'.format(pc))
elif op == '3' and pc == '1':
    print('\033[33mPC GANHOU!\033[m, PC ESCOLHEU {}'.format(pc))
elif op == '1' and pc == '3':
    print('\033[32mJOGANDOR GANHOU!\033[m, PC ESCOLHEU {}'.format(pc))
