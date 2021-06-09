#desenvolva um pograma que mostre as duas notas de um aluno calcule, e mostre a sua média
np1 = float(input('Me diga sua nota da np1:'))
np2 = float(input('Me diga a sua notada np2:'))
print('Sua média é ', float((np1+np2)/2 ))
#outra forma
'''resultado = (np1+np2)/2
print('Sua média é {}'.format(resultado)'''

#essa linha de baixo não esta na aula eu ja sabia
if (np1+np2)/2 >=6:
    print('Parabéns você passou!')
if (np1+np2)/2 ==5:
   print('Encima em!')
if (np1+np2)/2 <=4:
    print('Estude mais um pouco')
if (np1+np2)/2 == 0:
    print('orra! o trem ta fei')