#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
n1 = float(input('Quanto voce tirou na primeira prova?'))
n2 = float(input('Quanto voce tirou na sgunda prova?'))
media = (n1+n2) / 2
if media < 5.0:
    print('Sua média é {}\nPor isso está \033[31mREPROVADO\033[m!'.format(media))
elif 7 > media >= 5:#media <=5.0 and media > 7:
    print('Sua média é {}. \nPor isso está de \033[33mRRECUPERAÇÃO\033[m!'.format(media))
elif media >= 7.0:
    print('Parabéns sua média é {}\nVocê esta \033[32mAPROVADO\033[m!'.format(media))
