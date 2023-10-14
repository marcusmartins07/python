#      0123456789
frase='Curso em Vídeo Python'
print(frase)
print(frase[9]) #imprime somente uma letra
print(frase[9:13]) #imprime valor do escopo menos a ultima letra
print(frase[9:21:2]) #Começo no 9 paro no 21 e vou pulando 2 casas
print(frase[:5]) #Começa do 0 e vai até o 5
print(frase[15:]) #Começa do 15 até o final
print(frase[9::3]) #Começa no 9 e vai até o final pulando 3 casas

#Analise
print(len(frase)) #entrega o numero de caracteres
print(frase.count('o')) #Entrega o numero de caracteres definido
print(frase.count('o',0,13)) #Entrega o numero de caracteres definido a partir do escopo
print(frase.find('deo')) #vai indicar onde achou as letras
print(frase.find('android')) #se não encontrar ele entrega o valor -1
print('Curso' in frase) #retorna false ou true

#transformação
print(frase.replace('Python', 'Android')) #procura e substitui
print(frase.upper()) # Letras em maiusculo
print(frase.lower()) # Letras em minusculo
print(frase.capitalize()) # Só a primeira letra em maiusculo
print(frase.title()) # Onde tiver espaço a proxima letra sera maiusculo

frase = '   Aprenda Python  '
print(frase)
print(frase.strip()) # Remove espaços vazios
print(frase.rstrip()) # Remove espaços vazios a direita
print(frase.lstrip()) # Remove espaços vazios a esquerda

frase='Curso em Vídeo Python'
frase2 = frase.split() # Divide os espaços em uma lista
print(frase2) 
frase2 = '-'.join(frase2) # Inseri caractere no espaço entre lista
print(frase2)






