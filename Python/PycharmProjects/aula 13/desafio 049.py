#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
print('TABUADA')
m = int(input('Digite um numero:'))
print('==='*4)
for n in range(0, 10):
    print('{} x {} = {}'.format(n, m, n*m))
print('==='*4)