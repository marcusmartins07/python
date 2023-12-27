# Named tuple -> São tuplas, diferenciadas, onde especificamos um nome para a mesma e tamém parametros

from collections import namedtuple

# definir nome e parametros

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro',  'idade raca nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

#Acessando os dados

# Forma 1
print(ray[0]) # idade
print(ray[1]) # caça
print(ray[2]) # nome

# Forma 2
print(ray.idade) # idade
print(ray.raca) # raca
print(ray.nome) # nome