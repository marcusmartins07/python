"""
Iterator -> objeto que pode ser iterado
            retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterable -> um objeto que irá retornar um iterator quando a função iter() for chamada
"""

# É um iterable mas não é um iterator
nome = 'Geek'
numeros = [1, 2, 3, 4, 5, 6]

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

name = 'Geek'
for letra in nome:
    print(f'{nome}')