
# reduce não é mais uma função integrada, necessário importar

# reduce (função, dado) 

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# pode ser uma lambda ou função
multi = lambda x, y: x *y

res = reduce(multi, dados)
print(res)