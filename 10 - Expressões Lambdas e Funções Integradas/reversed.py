"""
Reversed = Só funciona em listas
Reversed = Funciona com qualquer iterável
"""

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# Converter para retornar lista

print(list(reversed(lista)))

print(tuple(reversed(lista)))

print(set(reversed(lista))) # Em conjunto não define ordem dos elementos

#Iterar
for letra in reversed('Geek University'):
    print(letra, end='')
print('\n')

print('Geek University'[::-1])

