#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista_de_numeros = []

while True:
    numeros = int(input('Digite um número:'))

    lista_de_numeros.append(numeros)

    lista_de_numeros.sort(reverse=True)

    condição_de_parada = ' '

    if condição_de_parada not in 'SN':

        condição_de_parada = str(input('Diseja continuar?[S/N]')).strip().upper()[0]

        if condição_de_parada == 'S':
            continue
        elif condição_de_parada == 'N':
            break


print('==='*15)
print(len(lista_de_numeros), ' números foram digitados')
print(f'A lista de números de tras para frente: {lista_de_numeros}')
if 5 in lista_de_numeros:
    print(f'O número 5 aparece na lista {lista_de_numeros.index(5)} vezes')
else:
    print('O número 5 não aparece na lista')
print('==='*15)

