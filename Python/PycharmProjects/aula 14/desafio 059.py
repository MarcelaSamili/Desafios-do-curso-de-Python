#Crie um programa que leia dois valores e mostre um menu na tela:
'''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa'''
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
print('MENU')
v1 = float(input('Digite um valor:'))
v2 = float(input('Digite outro valor:'))
resposta = 0
#n = [v1,v2]
multiplica = 0
while resposta != 5:
    resposta = int(input('''[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n>>>>O que voce que fazer?'''))#essas opções poderiam ser num print(), ue tb ira funcionar
    if resposta == 1:
        soma = v1 + v2
        print('a soma de {} + {} é {}'.format(v1, v2, soma))
    if resposta == 2:
        multiplica = v1 * v2
        print('O número {} x {} = {:.2f}'.format(v1,v2,multiplica))
    if resposta == 3:
        if v1 > v2:
            print('{} é maior'.format(v1))
        else:
            print('{} é maior'.format(v2))
    if resposta == 4:
        v1 = float(input('Digite um valor:'))
        v2 = float(input('Digite outro valor:'))
    elif resposta == 5:
        print('FINALIZANDO...')
        sleep(1)
    print('==='*10)
    sleep(1)
print('OK! FIM DO PROGRAMA.')





