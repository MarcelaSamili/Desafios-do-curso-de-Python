# jogo da forca
from random import choice
forca = """
_____
    |
    -"""
vazio = """


"""


cabeca = """
    O
"""
tronco = """
    O
    |
"""
braco_esquerdo ="""
    O
   /|
"""
braco_direito = """
    O
   /|\
"""
perna_direita = """
    O
   /|\
     \
"""
perna_esquerda = """
    O
   /|\
   / \
"""

chances_do_boneco = [vazio, cabeca, tronco, braco_esquerdo, braco_direito, perna_direita, perna_esquerda]


solo = 1
junto = 2
print('Digite [1] para jogar solo') 
print('Digite [2] para jogar com um amigo')#não fiz o modo dois ainda você pode fazer e melhorar esse código como usar as def e módulos é só clonar ! bom trabalho!
modo = int(input('Qual modo quer jogar:'))
letras_acertadas = ''
letras_erradas = ''
acertos = erros = 0

if modo == 1:
    palavras = ['MALA', 'LIVRO', 'CAMA']
    escolha = choice(palavras)



    while acertos != len(escolha) and erros != len(escolha):
        l = ''
        for letra in escolha:
            if letra in letras_acertadas:
                l += letra
            else:
                l += '- '

        print(forca + chances_do_boneco[erros])

        print(l)

        letra = str(input('Digite um letra')).upper()

        if letra in escolha:
            print('Essa letra tem...')
            letras_acertadas += letra
            acertos += 1

        else:
            print('Essa letra não tem...')
            letras_erradas = letra
            erros += 1

    print(f'A palavra era {escolha}')


