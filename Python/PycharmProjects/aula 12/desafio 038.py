#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
print('==='*10)
print('Digite um número INTEIRO!')
print('==='*10)
n1 = int(input('primeiro número:'))
n2 = int(input('segundo número:'))
if n1 > n2:
    print('O \033[36mPRIMEIRO\033[m número é o maior!!')
elif n2 > n1:
    print('O \033[36mSEGUNDO\033[m número é maior'.format(n2,n1))
elif n1 == n2 or n2 == n1:
    print('\033[32mEsses número são IGUAIS!!')
else:
    print('\033[31mNão sei do que voce esta falando')