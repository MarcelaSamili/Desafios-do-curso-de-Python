def dobro(valor=0, formato=False):
    res = valor + valor
    return res if formato is False else moeda(res)


def metade(valor=0, formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)

def aumento(valor = 0, t = 0, formato=False):
    res = valor + (valor * t/100)
    return res if formato is False else moeda(res)


def diminuir(valor=0, t=0, formato=False):
    res = valor - (valor * t/100)
    return res if formato is False else moeda(res)

def moeda(valor, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
# esse replace serve pra substituir, nesse ex, mesmo, eu quero subistidir onde tive ponto, por virgula...

def resumo(valor=1, taxaa=10, taxad=5):
    print('='*30)
    print('Resumo Do Valor'.center(30))#.center == centralizado a 30 caracter
    print('='*30)
    print(f'Preço: {moeda(valor):>21}\nMetade: {metade(valor, True):>20}\nDobro: {dobro(valor, True):>21}\nAumentando {taxaa}%: {aumento(valor,taxaa, True):>12}\nDiminuindo {taxad}%: {diminuir(valor,taxad, True):>12}')
    print('=' * 30)
#pra fazer tabulação ao invez de usar o :>21, pode usar o \t, fica tudo certinho tb e é mais facil..