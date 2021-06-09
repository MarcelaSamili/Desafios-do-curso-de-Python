#Faça um algoritimo que leia um salario de um funcionario e mostre seu novo salario com 15% de aulmento
salario = float(input('Me diga seu salário e eu digo quanto ele fica com 15% de aumento:'))
aumento = salario * 0.15
total = salario + aumento
print('Seu salário agora é {}'.format(total))
# pode ser assim tb, [ aumento + (preço * 15 / 100)]
