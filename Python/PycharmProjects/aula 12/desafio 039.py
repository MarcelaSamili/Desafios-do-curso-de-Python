#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year
ano = int(input('Qual ano voce nasceu?'))
idade = atual-ano
if idade == 18:
    print('Você tem {} anos. Está na hora de se alistar!'.format(idade))
elif idade > 18:
    print('Você tem {} anos. Já passou {} anos de se alistar!'.format(idade,idade-18))
    print('Voce deveia ter se alisatdo em {}!'.format(atual-(idade-18)))
else:
    print('Você tem {} anos. Ainda falta {} anos para voce se alistar. \nSeu ao de alistamento é {}!'.format(idade,18-idade,(atual+(18-idade))))
