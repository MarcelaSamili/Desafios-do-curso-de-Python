#Escreva um programa par aprovar um emprestimo para comprar uma casa.
#O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#calcule o valor dasprestações,sabendo que ela não pode execer 30% do salario, ou então o emprestimovai ser negado.
casa = float(input('Qual o valor da casa?R$'))
salario = float(input('Qual o eu salário?R$'))
ano = int(input('Em quantos anos voce quer financiar?'))
prestação = casa / (ano *12)
minimo = salario * 30/100
print('Para pagar uma casa de {} em {} anos a prestação será de {:.2f}.'.format(casa,ano,prestação))
if prestação <= minimo:
    print('\033[32mEmprestimo CONSEDIDO!')
else:
    print('\033[31mEmprestimo NEGADO!')


#eu fiz assim tb da certo
'''print('Sendo ao \033[33mvalor da casa\033[m: R${}\nE o \033[33mseu salário\033[m: R${} '.format(casa,salario))
if prestação <= salario-0.3:
    print('Sua prestação fica R${:.2f} por mes \n\033[32mVoce tem condiçes de financiar'.format(prestação))
elif prestação > salario-0.3:
    print('Sua prestação é R${:.2f} por mes \n\033[31mVoce não tem condições de financiar\nSinto muito, \033[1;31mEMPRESTIMO NEGADO'.format(prestação))'''
