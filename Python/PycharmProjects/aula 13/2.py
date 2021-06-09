'''n = int(input('digite um numero:' ))
for c in range(0,n+1):
    print(c)
print('FIM')
i = int(input('INICIO:'))
f = int(input('FIM'))
p = int(input('PASSO'))
for c in range(i,f+1,p):
    print(c)
print('FIM')
for c in range(0,5):
    n = int(input('Digite um valor:'))
print('FIM')'''
s = 0
for c in range(0,4):
    n = int(input('Digite um numero:'))
    s = s+n
print('A samatoria de todos o valores é {}'.format(s))