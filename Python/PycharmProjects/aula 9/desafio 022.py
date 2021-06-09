#crie um programa que leia o nome completo de uma pessoa e mostre na tela:
#o nome com todas as letras maiusculas
#o nome com todas as letras minusculas
#quantas letras tem ao todo sem comsiderar os espaços
#quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome em maiusculo: {}'.format(nome.upper()))
print('Seu nome em minusculo: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
d = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(d[0],len(d[0])))
'''print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))'''
#a logica disso é que como o programa começa acontar de 0, eu estou dizendo com esse (' ') espaço que é pra ele contar quantas letras tem de 0 ate o espaço
#e como eu ja coloquei em cima .strip()pra elininar espaços inicias e finais inuteis vai da certo, mais o melhor jeito é o primeio ele é mais lógic também.
