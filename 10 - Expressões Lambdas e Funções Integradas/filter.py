# filter() -> Filtrar dados

# media
valores = 1, 2, 3, 4, 5, 6

media = (sum(valores)/len(valores))
print(media)

import statistics
# Media com mean()
# media = statistics.mean(media)

res = filter(lambda x: x > media, valores)
print(list(res))

print(f'Novamente {list(res)}') #Agora tem que retornar zerado

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
res= filter(None, paises)
print(list(res))

# utilizando lambda
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# filter pode retornar booleano

# Exemplo mais complexo

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "Bob132", "tweets": []},
    {"username": "Doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
] 

# Filtrar usuário inativos

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)