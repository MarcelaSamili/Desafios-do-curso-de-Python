def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite um numero iteiro válido\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuario deixou a opção em branco\033[m')
            return 0
        else:
            return n

def linha(tam=30):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL'.center(30))
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[m\033[36m{item}\033[m')
        c += 1
    print(linha())
    op = leiaint('\033[33mSua opição:\033[m')
    return op
