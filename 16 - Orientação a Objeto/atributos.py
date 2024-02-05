
class Lampada:
    #definindo atributos internos da clase = metodo construtor
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem # -> Atributo de instância
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Classe com atributos privados
class Acesso:

    def __init__ (self, email, senha):
        self.email = email
        self.__senha = senha

user = Acesso('user@gmail.com', '123456')

print(user.email)

try:    
    print(user.__senha)
except AttributeError as ae:
    print(ae)


# Atributos de Classe
    
class Produto:

    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('PLaystation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.imposto)
print(p2.imposto)
print(p1.valor)
print(p2.valor)

print(Produto.imposto) # forma correta de consultar um atributo de classe


# Atributos Dinamicos

p3 = Produto('PLaystation 5', 'Video Game', 5000)

#Criando atributo dinâmico
p3.peso = '5Kg'

print(f'Produto: {p3.nome}, Descrição: {p3.descricao}, Valor: {p3.valor}, Peso: {p3.peso}')

try:
    print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
except AttributeError as ae:
    print(ae)


# Deletando atributos dinamicos
    
print(p2.__dict__)
print(p3.__dict__)

del p3.peso
del p2.descricao

print(p2.__dict__)
print(p3.__dict__)
