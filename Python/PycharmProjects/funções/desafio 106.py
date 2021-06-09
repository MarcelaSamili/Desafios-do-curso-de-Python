# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

#meu jeito
'''from time import sleep
def ajuda(msg):
    print('\033[1;34;40m-'*35)
    print(f'Acessando o manual da funcao "{msg}"...')
    print('-'*35)
    print('\033[m')
    sleep(1)

    print('\033[1;44m')
    help(msg)
    print('\033[m')
    return msg


while True:
    print('\033[36m='*24)
    print('Sistema de ajuda Pyhealp')
    print('='*24)
    print('\033[m')

    aj = str(input('Função ou Bibliotca >'))
    if aj.upper() in 'FIM':
        print('\033[31mAte logo!\033[m')
        break
    else:
        ajuda(aj)'''

#jeito da aula
from time import sleep
cores = ('\033[m',         # nenhuma cor
        '\033[36m',        # azul claro
        '\033[1;33;46m',   # fundo azul claro com letra amarela
        '\033[31m',        # letra vermelha
        '\033[33m',         # letra amarela
         '\033[7;40m')      # fundo branco


def ajuda(cod):
    titulo(f'Acessando o manual do comando \'{cod}\'', 4)
    print(cores[5], end='')
    help(cod)
    print(cores[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(cores[0], end='')
    sleep(1)


while True:
    titulo('Sistma de ajuda PYhealp', 1)
    aj = str(input('Função ou Biblioteca >'))
    if aj.upper() in 'FIM':
        break
    else:
        ajuda(aj)
titulo('Até logo!', 3)