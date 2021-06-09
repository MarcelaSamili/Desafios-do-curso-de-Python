# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    c = len(msg)
    print('-' * c + '--')
    print(msg)
    print('-' * c + '--')
escreva(' MERRY CRHISTIMAS')
escreva(' HAPPY BHIRDAY')
escreva(' O TODO É MENTE O UNIVERSO É MENTAL')
escreva(' OLÁ MUNDO! ME AGUARDE ')