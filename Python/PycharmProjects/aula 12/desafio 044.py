#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
'''à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros'''
valor = float(input('Quanto custa o produto?R$'))
print('''DIGITE: 
[1] para A VISTA DINHEIRO
[2] para CATAO A VISTA
[3] para ATE 2X NO CARTAO'
[4] para 3X OU MAIS NO CARTAO''')
pagamento = int(input('Como voce quer pagar?'))
'''if pagamento == 1:
    desconto1 = valor - (valor*10/100)
    print('Voce vai receber 10% de desconto')
    print('Com o desconto voce vai pagar R${}'.format(desconto1))
elif pagamento == 2:
    desconto2 = valor - (valor*5/100)
    print('Voce vai receber um desconto de 5%')
    print('Com o desconto o valor a pagar é R${}'.format(desconto2))
elif pagamento == 3:
    print('Pagando 2x no cartao.\nVoce pagará o valor formal do produto que é R${}'.format(valor))
elif pagamento == 4:
    juros = valor + (valor*20/100)
    print('Pagando em 3x ou mais no cartao voce terá um juros de 20%.')
    print('O valor final ficará a R${}'.format(juros))
else:
    print('O número que digitou não é um valor válido!')
    print('Tente novamente!')'''
#OUTRA FORMA
if pagamento == 1:
    total = valor - (valor*10/100)
elif pagamento == 2:
    total = valor - (valor*5/100)
elif pagamento == 3:
    total = valor
    parcela = total / 2
    print('Parcelando em 2x o valor de sua parcela é R${:.2f} cada.'.format(parcela))
elif pagamento == 4:
    total = valor + (valor*20/100)
    vaparcela = int(input('Em quantas parcelas voce quer pagar?'))
    parcela = total / vaparcela
else:
    total = valor
    print('\033[31mOPÇÃO INVÁLDA')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor,total ))