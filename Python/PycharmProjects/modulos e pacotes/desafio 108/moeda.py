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