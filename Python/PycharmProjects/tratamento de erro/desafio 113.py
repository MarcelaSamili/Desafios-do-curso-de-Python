#Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from leia import valores

n1 = valores.leiaint('Digite um número inteiro:')
n2 = valores.leiafloat('Digite um valor Real:')
print(f'O numero inteiro digitado foi {n1} e o Real foi {n2}')



