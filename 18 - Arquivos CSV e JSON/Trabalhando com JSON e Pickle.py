import json
import jsonpickle

# dumps = formata lista para padrão de aspa dupla JSON

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])
print(type(ret))
print(ret)

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
felix = Gato('Feliz', 'Vira-Lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)
print(ret)

# Escrevendo arquivo json/pickle

ret = jsonpickle
print(ret)

local_arquivo = '18 - Arquivos CSV e JSON/felix.json'

with open(local_arquivo, 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


# Lendo  arquivo json/pickle

with open(local_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)