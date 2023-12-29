"""
Estruturas de dados:
    - Unidimensionais (Arrays/Vetores);
    - Bidimenssionais (Matrizes)

Python Listas:
numeros = [1, 'b', 3.234, True, 5]
"""

listas= [[1,2,3], [4,5,6], [7,8,9]] #Matriz 3 x 3

print(listas)

print(listas[0][1]) #2 listas[linha][coluna]

# Iterando com loops
for lista in listas:
    for num in lista:
        print(num)

# List comprehension
[[print(valor) for valor in lista] for lista in listas]

# Gerando matriz 3 X 3

tabuleiro = [[numero for numero in range(1, 4) for valor in range(1, 4)]]
print(tabuleiro)

