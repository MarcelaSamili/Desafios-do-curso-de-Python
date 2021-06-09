#faça um prgrama que leia um numero de 0 a 9999 e mostre na tela cada umero separado
#unidade, desena, centena e milhar
n1 = int(input('Digite um numero:'))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('A unidade é {}'.format(u))
print('Desena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
#se voce tentar dividir em float não da certo DEVE SE EM INT pra da Certo.




