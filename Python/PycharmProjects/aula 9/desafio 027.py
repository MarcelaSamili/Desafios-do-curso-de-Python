#Faça um programa que leia no nome completo de uma pessoa e mostre o primero e ultimo nome
nome = str(input('Qual é o seu nome?')).title().split()
print('seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[-1]))
#o -1, quer dizer que ele vai começar contar da direita para a esquerda,ele vai começar ler a str de tras par fente
#pois os numero positivos são contados da esquerda para direita e negtvos da direita paraa esquerda
