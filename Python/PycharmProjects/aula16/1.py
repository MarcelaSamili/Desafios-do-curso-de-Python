lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
print(lanche[0])
#Tuplas sao imutvel
for comida in lanche:
    print(f'Vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('comi muito')
len(lanche)
for cont in range(0,len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

print(sorted(lanche))#sorted é odendo

a = (2,7,8)
b = (1,4,2)
c = a + b
print(c)# aqui ele vai JUNTAR as das tuplas = 2,7,8,1,4,2
print(c.count(2))#isso é pra contar quantas vezes aparece o 2
print(c.index(8))#isso é pra mostrar a posição, tipo o 8 esta naposição 2 ele vai mostrar isso
#pode colocar dados diferentes na mesma tupla EX:
pessoa = 'Marcela',19,'F', 'peso', 40 , 'Maravilhosa'
print(pessoa)
#del(pessoa), isso apaga completamente essa tupla
# a tupla é imutavel pq, por exeplo voce quer apagar somente MARCELA da tupla pessoa ai coloca 'del(pessoa[0])' isso não da
# ou tipo quiser mudar marcela(pessoa[0]) deixe de ser marcela e passe a ser ana assim (pessoa[0] = 'ana'. Isso nao da tb
