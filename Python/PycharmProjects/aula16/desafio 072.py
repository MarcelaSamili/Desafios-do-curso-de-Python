nunex = 'zero', 'um','dosi','tres','quatro','cinco','seis','sete','oito','nove','dez'\
,'onze','doze','treze','quatorze','quinse','dezesseis','dezessete','dezoito','dezenove','vinte'
while True:
    n = int(input('Digite um número entre 0 e 20:'))
    if n > 20 or n < 0:
        n = int(input('Digite um número entre 0 e 20:'))
    print(f'Você digitou o número {nunex[n]}.')
    c = str(input('que coninuar[S/N]')).strip().upper()[0]
    if c != 'S' or c == 'N':
        break






