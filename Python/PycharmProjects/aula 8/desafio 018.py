#Faça um programa que leia um angulo qualquer e mostre na tela o valo de seno, cosseno e tangente
import math
angulo = float(input('Digite uma agulo:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
hipo = math.hypot(math.radians(angulo))
print('Seno: {:.4f}'.format(seno))
print ('Cosseno: {:.4f}'.format(cosseno))
print('Hipotenusa: {:.4f}'.format(hipo))