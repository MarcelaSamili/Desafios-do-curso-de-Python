#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''n = ''
sexof = 'F'
sexom = 'M'
while n != sexof and n != sexom:
    n = str(input('Digite seu sexo [F/M]:')).upper().strip()[0]
    if n != sexof and n != sexom:
        print('INVALIDO')
print('Dado regitrado co sucesso.)'''
# jeito da aula
sexo = str(input('Informe seu sexo:[F/M]')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dado inválido, digite se sexo novamente:[F/M]')).strip().upper()[0]
print('Seu sexo é {}, e foi registrado com sucesso'.format(sexo))
