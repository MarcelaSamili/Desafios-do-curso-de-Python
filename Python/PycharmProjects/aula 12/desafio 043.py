#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
'''IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida'''
peso = float(input('Qual é o seu peso?(Kg)'))
altura = float(input('Qual a sua altura:(m)'))
imc = peso / (altura**2)
if imc <= 18.5:
    print('Seu IMC é {:.2f}'.format(imc))
    print('O voce esta \033[34mABAIXO\033[m do peso')
elif imc <=25:#o motivo de assim esta certo é que um comando não elimina o outro, entao ele vai ler menor que 25 ate 18.5 que é o outro comando.
    print('Seu IMC é {:.2f}'.format(imc))
    print('Você está no \033[32mPESO IDEAL\033[m')
elif imc <=30:
    print('Seu IMC é {:.2f}'.format(imc))
    print('Você está no \033[33mSOBREPESO\033[m')
elif imc <=40:
    print('Seu IMC é {:.2f}'.format(imc))
    print('Você está na \033[31mOBESIDADE\033[m')
else:
    print('Você está na \033[35mOBESIDADE MORBIDA!!CUIDADO!!\033[35m')