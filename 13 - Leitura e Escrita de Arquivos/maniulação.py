import os

# Verificando se diretorio ou arquivo existe
print(os.path.exists('arquivo.txt'))
print(os.path.exists('C://Users/Marcus Martins/Documents/Estudos/python publico/python/13 - Leitura e Escrita de Arquivos/texto.txt'))
print(os.path.exists('C://Users/Marcus Martins/Documents/Estudos/'))

caminho = 'C://Users/Marcus Martins/Documents/Estudos/python publico/python/13 - Leitura e Escrita de Arquivos/'

# Criando arquivo
with open(f'{caminho}arquivo-teste.txt', 'a') as arquivo:
    pass # ignorar ação dentro do bloco

# Criando diretorio
# os.mkdir(f'{caminho}pasta-teste') #apresenta erro se pasta ja existir

# Renomear arquivos e diretorios
# os.rename(f'{caminho}pasta-teste', 'pasta-teste2')

# Remover arquivos
# os.remove(f'{caminho}arquivo-teste.txt')

# Remover diretorio
os.rmdir(f'{caminho}pasta-teste2')