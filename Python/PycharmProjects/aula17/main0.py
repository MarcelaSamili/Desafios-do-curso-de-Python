'''inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
cont = 0
if inicio < fim:
    while inicio <= fim:
        inicio += 1
        print(inicio-1)
else:
    while inicio >= fim:
        inicio -= 1
        print(inicio+1)'''
#alunos
quantidade_de_aluno = int(input('Quants alunos tem na turma:'))
maior = menor = 0
cont = 0

while cont < quantidade_de_aluno:
    cont += 1


    print(f'ALUNO {cont}')
    nome = str(input('Digite o nome d aluno:')).strip().upper()
    nota = int(input('Digite a nota:'))

    if cont == 1:
        maior = menor = nota

    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota



    print('A maior nota foi {}'.format(nota))



