#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#um numero é primo somente se ele e for divisivel por 1 e por ele mesmo e por mais nenhum, entao ele so é divisivel 2vezes
n = int(input('Mediga um número:'))
total = 0
for c in range(1, n+1):#esse +1 é pq o python sempre conta um a menos dentro do for
    if n % c == 0:
        print('\033[32m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO {} foi divisivel {} vezes'.format(n, total))
if total == 2:
    print('\033[32mEsse é um número PRIMO!\033[m')
else:
    print('\033[31mEsse número NAO é primo!\033[m')