# Metodo dunder init = __ini__ é um método especial chamado de construtor e sua função é construir o objeto a partir da Classe

class Lampada:
    #definindo atributos internos da clase = metodo construtor
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem # -> Atributo de instância
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador = +1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha = cryp.encrypt(senha, rounds=20000, salt_size=16)
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

user1 = Usuario('Angelina', 'Jolie', 'angelinajolie@gmaill.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicityjones@gmail.com', '654321')

print(user1.nome_completo())
print(Usuario.nome_completo(user2))

# Acesso de forma errada de um atributo de classe
print(f'Senha User 1: {user1._Usuario__senha}')
print(f'Senha User 2: {user1._Usuario__senha}')


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador= +1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        return(self.__valor * (100 - porcentagem)) / 100
    
p1 = Produto('Playstation 4', 'Video Game', 2300)

print(p1.desconto(50))

print(Produto.desconto(p1, 40)) #self, desconto
