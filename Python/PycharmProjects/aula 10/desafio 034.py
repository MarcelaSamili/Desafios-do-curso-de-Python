#desenvolva um programa que pergunte ao usuaro qual o salario e calcule o valor do seu almento
#para salarios acima de 1250 o almento é de 10%, para salarios abaixo de 1250 o almento é de 15%
#JEITO QUE EU RESOLVI
'''salario = float(input('Quanto voce ganha?'))
if salario >= 1250:
    almento = salario * 10/100
if salario <= 1250:
    almento = salario * 15/100
print('Seu salario teve um almento de {} \ne seu salario agora e de {}'.format(almento,almento+salario)'''
# jeito da aula
salario = float(input('Qual é o seu salário?R$'))
if salario <= 1250:
    almento = salario + (salario * 15/100)
else:
    almento = salario + (salario * 10/100)
print('Seu salario era de R${:.2f} \nCom o almento ficou R${:.2f}'.format(salario, almento))