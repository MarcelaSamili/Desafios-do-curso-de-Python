# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    soma = computador + jogador
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Você quer par ou ímpar [P/I]')).upper().strip()[0]
    if pi == 'P':
        if soma % 2 == 0:
            print(f'Voce ganhou {computador} + {jogador} = {soma} par')
            v += 1
        else:
            print(f'Voce perdeu {computador} + {jogador} = {soma} impar')
            break
    if pi == 'I':
        if soma % 2 == 1:
            print(f'Voce ganhou {computador}+ {jogador} = {soma} impar')
            v += 1
        else:
            print(f'voce perdeu {computador} + {jogador} = {soma} par')
            break
print(f'Fim de jogo, voce ganhou {v} vez/veses')
