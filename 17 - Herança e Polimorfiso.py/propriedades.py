"""
POO - Propriedades - Properties
"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador+=10

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor
    
    # GET E SET

    # GET
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    # SET
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite



conta1 = Conta('Angelina', 3000, 5000)
conta2 = Conta('Felicity', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)