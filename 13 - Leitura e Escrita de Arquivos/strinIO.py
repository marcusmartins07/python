#StringIO -> Utilizado para ler e criar aruqivos em memoria

from io import StringIO

mensagem = "Esta é uma variavel comum"

# Podemos criar um arquivo em memoria ja com uma strin inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)
print(arquivo.read())

# Pode ser escrito outro texto
arquivo.write(' Outro texto')

# Movimentar cursor
arquivo.seek(0)
print(arquivo.read())