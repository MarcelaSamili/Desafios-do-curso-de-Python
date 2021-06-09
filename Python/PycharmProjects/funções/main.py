'''def soma(a, b):
    s = a + b
    print(s)


#progama principal
soma(5, 5)
soma(6, 2)
soma(7, 3)'''

'''def contador(* num):
    tam = len(num)
    print(f'Recebi {tam} valores e são eles {num}')


contador(5, 6, 9)
contador(6, 8, 4, 2, 0)
contador(2, 1)'''
#desse jeito ele vai guardar os valores em uma tupla

#da pra mexer com listas usando def tb:
#exemplo se eu tiver uma lista e precisar dobrar os valores nela, varias vezes no decorrer do codigo, eu posso fazer isso:
def dobra(lista):
    posição = 0
    while posição < len(lista):
        lista[posição] *= 2
        posição += 1


valores = [5, 6, 7, 8, 9, 2]
dobra(valores)
print(valores)