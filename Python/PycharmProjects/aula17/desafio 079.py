#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lvalores = []
while True:
    numeros = int(input('Digite um número:'))
    if numeros not in lvalores:
        lvalores.append(numeros)
        print('Numero adicionado')
    else:
        print('Numero duplicado nao adicionado')
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if q == 'S':
        print('\033[32mOk continuando...\033[m')
    elif q == 'N':
        break
lvalores.sort()
print(f'Os números adicionados foram: {lvalores}')