#Gerar novas listas a com dados processados de outro interável

"""sintaxe
dado for dado in interavel
"""

numeros = [1, 2, 3, 4, 5]
res = [numero*10 for numero in numeros]
print(res)

#list ccomprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])