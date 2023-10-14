from math import trunc

n=float(input('Digite um número: '))

print('O valor digitado foi {} e sua porção inteira é {:.0f}' .format(n, n))
print('O valor digitado foi {} e sua porção inteira é {}' .format(n, trunc(n)))
print('O valor digitado foi {} e sua porção inteira é {:.0f}' .format(n, int(n)))
