# Tuple Comprehension = Generators 

nomes = ['Carlos', 'Camila', 'Carol', 'Cassiano', 'Cristina', 'Vanessa']

print(all(nome[0] == 'C' for nome in nomes))

# ou
print(any(nome[0] == 'C' for nome in nomes))

#List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator -> Ocupa menos recurso em memória
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

from sys import getsizeof # retorna a quantidade de memoria em bytes utilizado

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
gen = getsizeof(x * 10 for x in range(1000))

print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# iterando
for num in gen:
    print(num)