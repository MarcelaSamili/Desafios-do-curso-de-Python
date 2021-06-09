import menud
from time import sleep

while True:
    try:
        menud.tela()
        op = int(input('Qual a sua opcao:'))
        menud.opicao(op)
        sleep(1)
        if op == 3:
            break
    except (TypeError):
        print('\033[31mErro: O sistema aceita somete numeros Inteiros!\033[31m')
    except (ValueError):
        print('\033[31mErro: Digite um valor INTEIRO VALIDO(1,2 OU 3)!\033[m')

