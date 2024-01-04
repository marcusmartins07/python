
arquivo = open('C://Users/Marcus/Documents/python/13 - Leitura e Escrita de Arquivos/texto.txt')

#print(arquivo.read())

# Movimentando o cursor pelo arquivo
arquivo.seek(20)

#print(arquivo.read())

print(arquivo.readline()) # le o arquivo, linha a linha

print(arquivo.readline()) 
print(arquivo.readline()) 

#print(arquivo.readlines()) # passa para lista

# podemos utilizar para contar as linhas
linhas = arquivo.readlines() 
print(len(linhas))

print(arquivo.closed) #Retorna false se estiver aberto

#Sempre necessário fechar o arquivo
arquivo.close()
print(arquivo.closed) #Retorna True se estiver fechado