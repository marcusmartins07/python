# o bloco with serve para abrir o arquivo "internamente"

with open('C://Users/Marcus/Documents/python/13 - Leitura e Escrita de Arquivos/texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)