arquivo = open("dados.txt", "rt") #para ler oarquivo
arquivo = open("dados.txt", "wt+") #para escrver o aquivo, caso ele n exista criar


frase = []
frase.append('Olá \n')
frase.append('eu quero \n')
frase.append('cagarrr \n')

arquivo.writelines(frase)
print(arquivo.readline())
