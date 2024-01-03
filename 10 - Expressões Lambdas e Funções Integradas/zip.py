# zip = Cria um iterável que agrega elemento de cada um dos iteráveis passados como entrada em pares

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')
print(zip1)
print(type(zip1))

print(list(zip1))

print(tuple(zip1))
print(set(zip1))
print(dict(zip1))

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3) # Para de iterar quando os elementos do menor iterável acaba
print(list(zip1))