# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e
# qual foi a soma entre eles (desconsiderando o flag ou seja desconciderando o 999).
n = int(input('Digite um numero, [999] para parar:'))
soma = n - 999
termos = 0
while n != 999:
    n = int(input('Digite um número:'))
    soma = soma + n
    termos += 1
print('A soma dos números digitado é {}'.format(soma))
print('E foram digitados {} números'.format(termos))
# esse jeito não é recomendado pois a variavel soma esta recebendo o 999 do mesmo jeito prem ele diminui ele
# a melhor forma de resolver esse desafio esta naaula 15



