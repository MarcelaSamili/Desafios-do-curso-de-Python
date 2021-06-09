#Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.
from random import randint
#jeito da aula
lista = (randint(1, 11)), (randint(1, 11)), (randint(1, 11)), (randint(1, 11)), (randint(1, 11))
print('Os números sortiados foram: ', end='')
for n in lista:
    print(f'{n} ', end= ' ')
print(f'\nO maior número é {max(lista)}')
print(f'O menor número é {min(lista)}')

