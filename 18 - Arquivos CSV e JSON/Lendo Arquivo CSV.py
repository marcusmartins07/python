
# Não é o ideal 

with open('18 - Arquivos CSV e JSON/lutadores.csv', encoding="utf8") as arquivo:
    dados = arquivo.read()
    #print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

print('\n')

# Usando reader

from csv import reader

with open('18 - Arquivos CSV e JSON/lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # pula o cabeçalho

    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros')

print('\n')

# Dict Reader
        
from csv import DictReader
with open('18 - Arquivos CSV e JSON/lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    # Cada linha é um Ordered Dict

    for linha in leitor_csv:
        print(f'{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centimetros')