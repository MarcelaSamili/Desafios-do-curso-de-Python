#Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''n = int(input('Digite um número:'))
soma = n
cont = 1
media = 0
maior = n
menor = n
n1 = str(input('voce quer [qualquer coisa]parar ou [c]continuar:')).upper().strip()[0]
while n1 == 'C' :
    n = int(input('Digite um número:'))
    cont += 1
    soma = soma + n
    media = soma / cont
    if cont == 1:
       maior = n
       menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    n1 = str(input('voce quer [qualquer coisa]parar ou [c]continuar:')).upper().strip()
print('A média dos números digitados é {:.2f}'.format(media))
print('O maior número digitado é {} e o menor é {}'.format(maior, menor))'''

#jeito da aula
resp = 'S'
soma = cont = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número:'))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior= n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar?[S/N]'))
media = soma / cont
print('Voce digitou {} números e a média é {}'.format(cont, media))
print('O maior númeoro digitado é {} e o menor é {}'.format(maior, menor))