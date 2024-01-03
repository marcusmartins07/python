# Expressão Lambda = Função Anonima

# Função em Python

def funcao(x):
    return 3*x+1
print(funcao(4))

# Expressão Lambda
lambda x: 3*x+1 

# Como utilizar
calc = lambda x: 3*x+1
print(calc(4))

# Com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('  marcus   ', '  mArTiNs '))

# Pode ter uma ou nenhuma entrada

amar = lambda: 'Como não amar Python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1/ z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))
