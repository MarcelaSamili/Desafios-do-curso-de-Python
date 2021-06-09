#faça um programa que leia um ano qualquer e mostre se ele é bissexto
'''ano = int(input('Digite um ano:'))
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} Nao é Bissexto'.format(ano))'''
#ou
from datetime import date
ano = int(input('Digite um ano, coloque 0 se quiser o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} Nao é Bissexto'.format(ano))
