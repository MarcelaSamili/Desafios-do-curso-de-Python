#Crie um programa que pergunte o nome de uma pessoa e diga se tem silva no nome
nome = str(input('Digite seu nome:')).title().upper().split()
print('Vou anaizar se no seu nome tem Silva.')
print('Analizando seu nome...')
print('SILVA' in nome[0:])
