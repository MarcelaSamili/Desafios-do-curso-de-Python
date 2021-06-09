import moeda
#from desafio 107 import moeda

num = float(input('Digte um preço: R$'))
taxa = float(input('Qual a taxa:%'))
print(f'A metade de {num} é R${moeda.metade(num)}')
print(f'O dobro de {num} é R${moeda.dobro(num)}')
print(f'Aumentando {taxa}% de {num} temos R${moeda.aumento(num,taxa)}')
print(f'Diminuindo {taxa}% de {num} temos R${moeda.diminuir(num, taxa)}')