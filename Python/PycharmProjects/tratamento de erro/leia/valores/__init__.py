def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: digite um número inteiro válido!\033[m')
            continue
        else:
            return n


def leiafloat(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mErro: digite um número Real válido!\033[m')
            continue
        else:
            return n