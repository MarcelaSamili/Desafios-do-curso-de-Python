#O mesmo prfessor do ourto desafio quer sortear a ordem de aprsentaçoes dos seu quatro alunos.
#crie um probrama que leia o nome dos quatro alunos e leia a ordem sorteada
#modo direto
'''import random
apr1 = str(input('Digite o nome do primeiro aluno:'))
apr2 = str(input('Digite onome do segundo aluno:'))
apr3 = str(input('Digite o nome do terceiro aluno:'))
apr4 = str(input('Digite o nome do quarto aluno:'))
sorteio = [apr1, apr2, apr3, apr4]
random.shuffle(sorteio)
print('A ordem de apresetação  é:')
print(sorteio)'''
#modo direto
from random import shuffle
apr1 = str(input('Digite  nome do primerio aluno:'))
apr2 = str(input('Digito nome do seguno aluno:'))
apr3 = str(input('Digite o nome do terceiro aluno:'))
apr4 = str(input('Digite o nome do quarto aluno:'))
sorteio =  [apr1,apr2,apr3,apr4]
shuffle(sorteio)
print('A ordem de apresentação é:')
print(sorteio)



