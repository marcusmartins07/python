# ordenando em ordem crescente
numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))

# ordenando em ordem decrescente
numeros = {6, 1, 8, 2}
print(numeros)
print(sorted(numeros, reverse=True))

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "Bob132", "tweets": []},
    {"username": "Doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
] 

print(sorted(usuarios, key=lambda usuario: usuario["username"]))