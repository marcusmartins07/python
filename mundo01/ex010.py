import math
# from math import sqrt
# from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,raiz))
print('Arrendondando para cima = {} e para baixo = {}'.format(math.ceil(raiz), math.floor(raiz)))