#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#E mostre sua categoria, de acordo com a idade:
'''Até 9 anos: MIRIM ;Até 14 anos: INFANTIL; Até 19 anos: JÚNIOR; Até 25 anos: SÊNIOR; Acima de 25 anos: MASTER'''
from datetime import date
ano = int(input('Qual ano voce nasceu?'))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Voce tem {} anos'.format(idade))
    print('Voce é dacategoria MIRIM!')
elif idade <=14:
    print('Voce tem {} anos'.format(idade))
    print('Voce é da categoria INFNTIL!')
elif idade <= 19:
    print('Voce tem {} anos'.format(idade))
    print('Voce é da categoria JÚNIOR!')
elif idade <=25:
    print('Voce tem {} anos'.format(idade))
    print('Voce é da categoria SÊNIOR!')
elif idade >=26:
    print('Voce tem {} anos'.format(idade))
    print('Voce é da categoria MASTER!')


