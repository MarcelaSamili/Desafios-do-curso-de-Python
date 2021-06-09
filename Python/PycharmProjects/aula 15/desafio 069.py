#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
mi = 0
homem = 0
mulher = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]:')).strip().upper()[0]
    if idade >= 18:
        mi = mi + 1
    if sexo in 'Mm':
        homem = homem + 1
    if sexo in 'Ff':
        if idade < 20:
            mulher += 1
    cn = ' '
    while cn not in 'SN':
        cn = str(input('Quer continua[S/N]')).strip().upper()[0]
    if cn == 'S':
        print('---'*10)
        print('PROXIMO CADASTRO')
        print('---'*10)
    elif cn == 'N':
        break
print(f'Tiveram {mi} pessoas maiores de 18 e {homem} homens')
print(f'Tiveram tambem {mulher} mulheres mores de 20 anos.')

