"""
POO -> Objetos

Objetos -> São instâncias da classe, representação computacional de objetos reais

objeto ou instâcia são elementos que estão dentro das classes
"""
class Lampada:

    def __init__ (self, cor, voltagem, luminosidade): # -> Construtor
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    # Metodo
    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:
    
    #construtor
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    # metodo
    def diz(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class ContaCorrente:
    
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador = +1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class Usuario:
    
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha 


#Instancias / Objetos
    
lamp1 = Lampada('Branca', 110, 60)

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

user1 = Usuario('Felicity', 'Jones', 'felicityjones@gmail.com', '123456')
print(type(user1 ))

cli1 = Cliente('Angelina Jolie', '123.456.789-99')
cc1 = ContaCorrente(5000, 2000, cli1)

cc1.mostra_cliente( )
#cc1.ContaCorrente__cliente.diz()



