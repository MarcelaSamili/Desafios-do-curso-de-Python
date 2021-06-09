#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0,10)
print('\033[35m***'*13)
print('\033[34mOlá sou seu computador!')
print('Acabei de pensar em um número de O a 10!')
print('Tente adivinhar!!\033[m')
print('\033[35m***'*13)
jogador = int(input('\033[36mQual número eu pensei?\033[m'))
tentativas = 1
while jogador != computador:
    jogador = int(input('\033[36mTente de novo!:\033[m'))
    if jogador != computador:
        tentativas += 1
        if computador < jogador:
            print('\033[33mmenos...')
        else:
            print('\033[33mmais...\033[m')
    if jogador == computador:
        print('\033[32mVocê acertou!! Eu pensei no número {}!'.format(computador))
        print('Você precisou de {} tentativas para acertar\033[m'.format(tentativas))
print('\033[35mFim de jogo!\033[m')
#jeito da aula
'''from random import randint
computador = randint(0,10)
print('\033[35m***'*13)
print('\033[34mOlá sou seu computador!')
print('Acabei de pensar em um número de O a 10!')
print('Tente adivinhar!!\033[m')
print('\033[35m***\033[m'*13)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if computador > jogador:
            print('Mais...')
        else:
            print('Menos')
print('Voce acertou eu pensei no numero {}'.format(computador))
print('Voce precisou de {} tentativas'.format(palpite))'''


