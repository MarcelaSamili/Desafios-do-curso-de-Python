#Faça um programa que mostre o preço de um produto, e mostre seu nvo preço com 5% de desconto.
preço = float(input('Qual o preço original? R$'))
desconto = preço*0.05
total = preço - desconto
print('Sendo o preço original R${:.2f}, com o desconto de 5% fica a R${:.2f}'.format(preço, total ))
#pode ser assim tb,[ desconto = preço - (preço * 5 / 100) ]