#  Crie um programa que leia o ano de nascimento de sete pessoas.
#  No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
print('---'*7)
print('CALCULANDO MAIORIDADE')
print('---'*7)
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nsc = int(input('Ano da {}° pessoa:'.format(c)))
    if ano - nsc >= 18:
        maior += 1
    elif ano - nsc <18:
        menor += 1
print('{} pessoas atingiram a maior idade'.format(maior))
print('{} pessoas são menores de idade'.format(menor))
