# Max -> Retorna o maior valor em um interável ou o maior de dois ou mais elementos
# Min -> Retorna o menor valor em um interável ou o maior de dois ou mais elementos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario)) #f

print(max(dicionario.values())) #129

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Master of Puppets", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])