n1 = int(input('Me diga um valor'))
n2 = int(input('Me diga outro'))
a = n1 + n2
s = n1 - n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print( 'a soma de {} e {} \né {} a subutração é {} a divisão é {} a multiplicação é {}'.format(n1, n2, a, s, d, m), end=' ')
print ('a divisão inteira é {} o resto é {} e o exponecial é {}'.format(di, r, e))
#end='' quer dizer que vc quer continuar a lina e \n para nova linha