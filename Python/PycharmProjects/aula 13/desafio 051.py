#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('\033[34m10 TERMOS DE UMA PA!\033[m')
t = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razao:'))
decimo = t + (11 -1) * r
for c in range(t ,decimo, r):
    print(c, end=' - ')
print('FIM')
