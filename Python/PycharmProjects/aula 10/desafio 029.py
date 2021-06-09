#Crie um programa que leia a veloiade do carro
#Se ele assar de 80km/h mostre umamensagem dizendo que ele levou uma multa
#A multa va custar R$7,00 por ca da km acima do permitido
'''from random import randint#eu fiz como se um radar ou o propio corro lesse a velcidade sozinho
vc = randint(0,250)
print('Seu carro esta a {}km/h'.format(vc))
if vc >80:
    print('VOCE ULTRAPASSOU O LIMTE DE 80KM/H o valor da multa é R${}'.format((vc-80)*7))
else:
    print('Continue respeitando o limite de velocidade!')'''
#eu fiz como se o pc estivese lendo a velocidade do carro
#resolção da aula
vc = int(input('Digite uma velocidade:km'))
if vc > 80:
    print('Voce esta além do limite de 80km')
    print('Nessa velocidade voce ganhou uma multa de R${}'.format((vc-80)*7))
else:
    print('VOCE ESTA DENTRO DO LIMITE, CONTINUE ASSIM!')
