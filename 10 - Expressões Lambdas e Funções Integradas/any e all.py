"""
all() -> retorna true se todos os elementos do interavel são verdadeiros ou ainda se o interavel estiver vazio
"""

print(all([0, 1, 2, 3, 4]))
print(all([1, 2, 3, 4]))
print(all([]))

nomes = ['Carlos', 'Camila', 'Carol', 'Cassiano']
print(all(nome[0] == 'C' for nome in nomes)) #list comprehension para verififcar lista

# any() -> retorna true se qualquer elemento do interavel for verdadeiro. Se o interavel estiver vazio retorna false
print(any([0, 1, 2, 3, 4])) 

print(any([0, False, {}, (), []])) 

