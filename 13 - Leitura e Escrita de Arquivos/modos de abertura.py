"""
Modos de abertura de arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo ja exista
x -> Abre para escrita somente se o arquivo não existir. Caso existe retorna FileExistsError
a -> (Append) Abre para escrita, adicionando o conteúdo ao final do arquivo. se o arquivo não existir, sera criado.
Caso exista, o novo conteúdo será adicionado ao final

"""

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo \n')
except FileExistsError:
    print('Arquivo já existe')

with open('frutas.txt', 'a+') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.seek(0) # cursor no inicio do arquivo
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
    
