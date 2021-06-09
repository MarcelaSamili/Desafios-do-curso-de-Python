#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
gc = float(input('Me diga a temperatura em c° que vc quer converter:C°'))
gf = (gc*9/5)+32
print('Analizando os dados {}C° valem {}°F'.format(gc,gf))