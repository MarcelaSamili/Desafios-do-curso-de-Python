#Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
lista_principal = []
d = {}
lista_gols = []
soma = 0
while True:
    d.clear()
    lista_gols.clear()
    d['nome'] = str(input('Nome do jogador:')).strip().title()
    partidas = int(input(f'Quantas partidas o {d["nome"]} jogou:'))
    for n in range(0, partidas):
        lista_gols.append(int(input(f' Quantos gols na partida {n+1}?')))
        soma = sum(lista_gols)
    d['gols'] = lista_gols[:]
    d['total'] = soma
    lista_principal.append(d.copy())

    while True:
        cond = str(input('Quer continuar?[S/N]:')).strip().upper()[0]
        if cond in 'SN':
            break
        print('ERRO! S ou N para resposta')
    if cond == 'N':
        break

print("-="*40)
print(f'{"Nº":<5}{"Nome":<10}{"Gols":<10}{"Total":>7}')
print("-"*40)
for i, j in enumerate(lista_principal):
    print(f'{str(i):<5}{str(j["nome"]):<10}{str(j["gols"]):<10}{str(j["total"]):>5}')
print("-"*40)
while True:
    dado = int(input('Quer ver os dados de qual jogador?(999 para parar)Nº:'))
    if dado == 999:
        break
    if dado >= len(lista_principal):
        print(f'O código {dado} não existe!')
    else:
        if dado <= len(lista_principal):
            print(f'LEVANTAMENTO DO JOGADOR {lista_principal[dado]["nome"]}.')
        for i, v in enumerate(lista_principal[dado]["gols"]):
            print(f'    -No {i+1}º jogo fez {v} gols')

print("-"*40)
#print(f'{i:<5}{v["nome"]:<10}{v["gols"]:<10}{v["total"]:>8}')
