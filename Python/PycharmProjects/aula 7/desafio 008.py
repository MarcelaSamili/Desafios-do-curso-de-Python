# escreva um programa que leia um valor em metros e exiba em centimetros e milimetros
# sem variavel
'''m = int(input('Mediga quantos metros e eu digo sua equivalencia em cm² e mm'))
#print(m * 100,'cm²', m * 1000, 'mm' )'''

#com varavel
m = float(input('Me diga uma medida em m² e eu digo sua equivalncia em cm² e mm:'))
cent = m * 100
mm = m * 1000
print('Sua equivalencia me cm² é {:.2f}'.format(cent))
print('Sua equivalencia em mm é {:.2f}'.format(mm))