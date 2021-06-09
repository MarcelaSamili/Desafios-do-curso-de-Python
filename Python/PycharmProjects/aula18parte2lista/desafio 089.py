# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

'''lista_notas = []
nota = []
botetim = []
lista_alumed = []
lista_aluno = []
aluno1 = []
while True:
    aluno = str(input('Nome do aluno:')).strip().title()
    np1 = float(input('Primeira nota:'))
    np2 = float(input('Segunda nota:'))
    nota.append(np1)
    nota.append(np2)

    media = (np1 + np2) / 2
    lista_alumed.append(aluno)
    lista_alumed.append(media)
    botetim.append(lista_alumed[:])#lista com alunos e medias juntos
    lista_alumed.clear()

    lista_notas.append(nota[:])# lista so com medias
    nota.clear()

    aluno1.append(aluno) # lista so com alunos
    lista_aluno.append(aluno)
    aluno1.clear()

    cadastro = ' '
    if cadastro not in 'N':
        cadastro = str(input('Quer cadastrar mais algum aluno?:[S/N]')).strip().upper()[0]
        if cadastro in 'N':
            break
cont = 0
print('==='*20)
for b in botetim:
    print('Nº    nome       média')
    print(f'{cont}    {b[0]:^6}      {b[1]:^6}')
    print('---'*9)
    cont += 1

cond = ' '
while cond not in 'P':
    noalu = int(input('Voce quer ver as notas do aluno número? Nº:'))
    print(f'{lista_aluno[noalu]} tirou: {lista_notas[noalu]}')
    cond = str(input('Quer continuar?[C/P]:')).strip().upper()[0]
    if cond in 'P':
        break'''

#jeito da aula
lista = []
while True:
    aluno = str(input('Nome do aluno:')).strip().title()
    np1 = float(input('Primeira nota:'))
    np2 = float(input('Segunda nota:'))
    media = (np1 + np2) / 2
    lista.append([aluno, [np1, np2], media])
    resp = str(input('Quer continuar:[S/N]'))
    if resp in'Nn':
        break
print('==='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('---'*26)
for i, a in enumerate(lista):
    print(f'{i:<4}    {a[0]:<10}      {a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = str(input('Mostrar a nota de qual aluno? (999 para parar) Nº:'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista):
        print(f'As notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<<VOLTE SEMPRE!>>>>')





