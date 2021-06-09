# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Qualtos KM voce percorreu com o carro?KM'))
dias = int(input('Quantos dias voce alugou o carro?'))
preço = (60*dias) + (0.15*km)
print('O valor do aluguel ficou em R${}'.format(preço))
