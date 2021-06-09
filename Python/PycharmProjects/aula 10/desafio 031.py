#desenvolva umprograma que pergunte a distancia da viagem em km.Calcule o preço da viagem cobrndo R$0.50
#por km em viagem de ate 200km e R$0.45 em vigens mais longas
'''d = float(input('Quantos km tem sua viage?Km'))
if d <= 200:
    print('Sua vigem vai ter um custo de R${} Reais '.format(d*0.50))
if d > 200:
    print('Sua viagem vai ter um custo de R${:.2f} Reais.'.format(d*0.45))
print ('==='*5)
print('BOA VIAGEM!! ')
print('==='*5)'''
#resolução da aula
d = float(input('Qual é a diatancia da sua viagem?Km'))
if d <= 200:
    preço = d*0.50
else:
    preço = d*0.45
print('Sua viagem tem um custo de R${:.2f} Reais'.format(preço))
print('==='*5)
print('BOA VIAGEM!!')
print('==='*5)
#outra maneira é
'''d = float(input('Quantos km tem sua viage?Km'))
preço = d*0.50 if d <=200 else d *0.45
print('Sua viagem vai ter um custo de R${:.2f} Reais.'.format(preço))
print ('==='*5)
print('BOA VIAGEM!! ')
print('==='*5)'''