#u professor quer sortear um dos seus quatro aluno para apagar o quadro.
# Faça um programa que pergunte nome deles e com isso ele de o nome dosorteado na tela.
import random
n1 =str(input('Nome do primeiro:'))
n2 = str(input('Nome do segundo:'))
n3 = str(input('Nome do terceiro:'))
n4 = str(input('Nome do quarto:'))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O sorteado é {}'.format(escolhido))



