c = v = 0
while True:
    n = int(input('Digite um número [999 para parar]:'))
    if n == 999:
        break
    c = c + n
    v += 1
print(f'A soma dos {v} números é {c}')