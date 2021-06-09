#Crie um programa que pergunte quanto dinheiro uma pesssoa tem na carteira, e mostre quantros dólares ela pode .
#considere US1,00 = R$ 5,65
r = float(input('Me diga quanto voce tem na carteira, em Reais, e eu digo quantos dólares você pode comprar: R$'))
d = r / 5.65
print('Estando 1 dólar a 5,65 reais, você poderá comprar com R$ {}, US$ {:.2f} .'.format(r,d))