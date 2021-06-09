# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número inteiro:'))
print('Digite 1 para birnario.')
print('Digite 2 para octal')
print('Digite 3 para Hexadecimal.')
escolhido = int(input('Qual voce escolhe?'))
if escolhido == 1:
    print('Beleza vou converter para \033[1;32mBIRNÁRIO')
    print('O número {} convertido para \033[1;32mBIRNÁRIOé {}'.format(n,bin(n)[2:]))
elif escolhido == 2:
    print('Beleza vou converter para \033[1;33mOCTAL')
    print('O número {} convertido fica para \033[1;33mOCTAL é {}'.format(n,oct(n)[2:]))
elif escolhido == 3:
    print('Beleza vou converter para \033[1;34mHEXADECIMAL')
    print('O número {} convertido para \033[1;34mHEXADECIML é {}'.format(n,hex(n)[2:]))
else:
    print('\033[31mOPÇÃO INVÁLIDA!')