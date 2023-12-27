# Tuplas são imutáveis

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

escola = tuple('Esta é uma frase')
print(escola)
print(escola.count('a'))

# Dicas de utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

#Exemplo 01

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#Acesso de elementos
print(meses[5])

""" for c in meses:
    print(meses[c]) """

