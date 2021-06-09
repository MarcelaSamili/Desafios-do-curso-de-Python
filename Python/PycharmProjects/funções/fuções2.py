#ajuda interativa
'''help(print)
print(input.__doc__)'''

#docstring

'''#voce pode criar uma função pra outras pessoas usarem,
# e se elas não souberem voce faz uma eplicação, dai quando elas usarem o help vai endanter como usar
#EXEMPLO
def contador(i, f, p): #vc criuou essa função contador, ai a pessoa nao entende o que é esse i, f, p ai vc fazr isso,
    """
    essa função faz contagem númerica
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
#fazendo isso qaundo a pessoa usar o comando help isso vai aparecer ai ela vai enteder
    cont = i
    while cont <= f:
        print(f' {cont}', end=' ')
        cont += p
help(contador)'''

#parametros opicionais

'''def soma(a=0, b=0, c=0):#isso é um parametro opcional, ou seja, caso eu nao declare algum dos pametros ele fica valendo zero.
# se voce nao fizer isso e nao declarar os tres, vai dar erro.
    s = a + b + c
    print(f'A soma é {s}')


soma(2, 3, 6)
soma(1, 2)
soma(1)
soma(c=2, b=5)'''

#escopo de varivel

#basicamente escop local é aquele que funciona somente dentro de uma função, e global funciona tanto fora como dentro, EX:
'''def teste(b):
    globol a
    a = 8
    b += 4
    c = 5
    print(f' A fora vale {a}')# escopo global
    print(f' A dentro vale {b}')# essa variavel b e c só funciona dentro do def entao elas são escopo local
    print(f' A dentro vale {c}')

a = 5 
teste(a)
print(f' A fora vale {a}')'''

# Retorndo resultados
''''def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = soma(2, 3, 6)
r2 = soma(2, 4)
r3 = soma(7)
print(f'Os retados das somas são: {r1}, {r2}, {r3}')'''

