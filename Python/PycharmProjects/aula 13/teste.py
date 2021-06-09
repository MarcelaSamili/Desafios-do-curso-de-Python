somaidade = 0
media = 0
maioridadehomem = 0
nomehvelho = ''
quantidademulher = 0
for i in range(1, 5):
    print('\033[33mPARTICIPANTE {}\033[m'.format(i))
    nome = str(input('Qual seu nome:')).upper().strip()
    idade = int(input('Qual sua idade:'))
    sexo = str(input('digite seu sexo [F/M]:')).strip()
    somaidade += idade
    media = somaidade / 4
    if sexo in 'Mm':
        if i == 1:
            maioridadehomem = idade
            nomehvelho = nome
        else:
            if idade > maioridadehomem:
                maioridadehomem = idade
                nomehvelho = nome
    if sexo in 'Ff':
        if idade < 20:
            quantidademulher = quantidademulher + 1
print('==='*20)
print('\033[32mA MÉDIA DE IDADE É :{}\033[m'.format(media))
print('\033[34mO homem mais velho é: {}\033[m'.format(nomehvelho))
print('\033[35mA quantdade de mulher que tem nenos que 20 anos é, {}\033[m'.format(quantidademulher))
print('==='*20)