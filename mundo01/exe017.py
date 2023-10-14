from math import hypot

co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))

h1 = ((co**2)+(ca**2))**0.5 
print('A hipotenusa vai medir {:.2f}'.format(h1))


h2 = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h2))


#12,25  22,56 = 34,81
