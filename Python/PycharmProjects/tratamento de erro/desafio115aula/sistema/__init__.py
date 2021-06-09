def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro somente numeros inteiros sao aceitos')
        else:
            return n

def linha(tam=30):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for intem in lista:
        print(f'{c} - {intem}')
    print(linha())
    opc = leiaint('Qual é a sua opição:')
    return opc
