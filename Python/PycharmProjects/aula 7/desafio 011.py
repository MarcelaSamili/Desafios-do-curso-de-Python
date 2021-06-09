#Desenvolva um programa que leia a largura e a altura de uma parede em metros e calcule a área, e a quantidade detinta necessária para pinta-la,
#sabendo que 1L de tinta pinta, 2m² de área.
largura = float(input('Qual é a largura dessa parede em m²?'))
altura = float(input('Qual a altura dessa parede em m²?'))
area = largura * altura
tinta = area / 2
print('Com base nos dados, sua parede tem {:.2f} m² de área. \nSendo assim, você vai precisar de {:.2f}L de tinta, para pintar toda ela.'.format(area,tinta))
