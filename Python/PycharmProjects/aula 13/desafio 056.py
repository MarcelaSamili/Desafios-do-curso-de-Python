# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
somaidade = 0
media = 0
maioridadehomem = 0
nomehvelho = ''
quantidademulher = 0
for i in range(1,5):
    print('\033[33mPARTICIPANTE {}\033[m'.format(i))
    nome = str(input('Qual seu nome:')).upper().strip()
    idade = int(input('Qual sua idade:'))
    sexo = str(input('digite seu sexo [F/M]:')).upper().strip()
    somaidade += idade
    media = somaidade / 4
    if i == 1 and sexo in 'M':
        maioridadehomem = idade
        nomehvelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehvelho = nome
    if sexo in 'F' and idade < 20:
        quantidademulher += 1
print('==='*20)
print('\033[32mA MÉDIA DE IDADE É :{}\033[m'.format(media))
print('\033[34mO homem mais velho é: {}\033[m'.format(nomehvelho))
print('\033[35mA quantdade de mulher que tem nenos que 20 anos é, {}\033[m'.format(quantidademulher))
print('==='*20)