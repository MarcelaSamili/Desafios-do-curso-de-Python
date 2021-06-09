#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

tot_lista = []
lista_pares = []
lista_impares = []
while True:
    valor = int(input('Digite um valor:'))
    tot_lista.append(valor)
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)

    cond = ' '
    if cond not in 'SN':
        cond = str(input('Quer continuar?[S/N]')).strip().upper()[0]
        if cond == 'N':
            break

print()
print(f'Lista de números digitdos: {tot_lista}')
print(f'Lista de números pares digitados: {lista_pares}')
print(f'Lista de números impares digitados: {lista_impares}')

#pode ser assim tb
'''tot_lista = []
lista_pares = []
lista_impares = []

while True:
    valor = int(input('Digite um valor:'))
    tot_lista.append(valor)
    cond = ' '
    if cond not in 'SN':
        cond = str(input('Quer continuar?[S/N]')).strip().upper()[0]
        if cond == 'N':
            break
for i, valor in enumerate(tot_lista):
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)
print()
print(f'Lista de números digitdos: {tot_lista}')
print(f'Lista de números pares digitados: {lista_pares}')
print(f'Lista de números impares digitados: {lista_impares}')'''
