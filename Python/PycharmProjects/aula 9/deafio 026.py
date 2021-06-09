#crie um programa que leia uma frase no teclado e mostre:
#quantas vezes aparee a letra 'A'
#Em que posição ela aprece a primeira e ultima vez
frase = str(input('Digite uma frase:')).strip().upper().rstrip().rstrip()
print('Essa frase tem {} letra(s) A.'.format(frase.count('A')))
print('O primeiro A aparece na posição {}'.format(frase.find('A')+1))#esse +1 é pq  programa começa a conar do 0
print('O ultimo A se encontra na posição {}'.format(frase.rfind('A')))#vai conta somente o 'a' quando ele aparece na direita