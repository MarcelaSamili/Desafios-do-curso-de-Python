#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('***'*10)
print('\033[36mMEGA SENA SORTEIOS ALTOMÁTICOS\033[m')
print('***'*10)
lista = []
sorteios = []
jogo = int(input('Quantos jogos quer fazer?:'))
for nsorteios in range(0, jogo):
    for cc in range(0, 6):
        sorteio = randint(1, 60)

        sorteios.append(sorteio)
        print(sorteios)
    lista.append(sorteios[:])
    sorteios.clear()
cont = 0
print(f'    \033[32mSORTEANDO OS {jogo} JOGOS\033[m')
for p in lista:
    cont += 1
    sleep(1)
    print(f'jogo {cont}:{p}')
print('{:=^32}'.format("BOA SORTE!!"))



