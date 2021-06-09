#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
numeros = list()

def sorteia(lista):
    print('Os números sorteados são:', end=' ')
    for c in range(0, 5):
        s = randint(1, 11)
        numeros.append(s)
        sleep(0.5)
        print(f'{s}', end=' ')
    print()
def somapar(lista):
    soma = 0
    for v in lista:
        if  v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de: {numeros}')
    print(f'E a soma dos pares é {soma}')


sorteia(numeros)
somapar(numeros)
