#Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(*num):
    print('='*40)
    print('Analizando valores..')
    maior_numero = max(num)
    print(f'Os numeros digitados foram:', end=' ')
    for n in num:
        sleep(0.4)
        print(f' {n} ', end=' ')
    print(f'Foram {len(num)} passados ao todo,')
    print(f'E o maior é o numero {maior_numero}.')


maior(7, 1, 2, 6, 9)
maior(1)
maior(100, 5, 6, 8, 7, 101)
maior(3, 2, 4)
maior(1, 2)
maior(0)