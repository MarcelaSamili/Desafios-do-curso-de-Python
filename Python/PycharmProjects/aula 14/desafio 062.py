#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
from time import sleep
p= int(input('Digite o Primeiro número:'))
r = int(input('Digite a rasão:'))
termo = p
cont = 1
total = 0
t2 = 10
while t2 != 0:
    total = total + t2
    while cont <= total:
        print('{} - '.format(termo), end=' ')
        termo += r
        cont += 1
    print('Pause')
    t2 = int(input('\nVoce quer mostrar mais quantos termos:'))
print('fINALIZANDO...')
sleep(1)
print('O total de termos mostrasdos foi de {}'.format(total))
