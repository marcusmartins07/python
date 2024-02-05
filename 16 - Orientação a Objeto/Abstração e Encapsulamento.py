"""
POO - Abstração e Encapsulameto

O grande objetivo da POO é encapsular nosso código dentro de um grupo çógico e hierárquico utilizando classes

dentro das classes temos (atributos e métodos)



Atributos / métodos privados

atributo privado = __nome
método privado = __falar()

Exemplo acessando metodos privados. Em outras linguagens não é possível realizar o acesso
instancia._Pessoa__nome
instancia._Pessoa__falar()

Abstração = Expor apenas dados relevantes de uma classe, escondendo tributos e métodos privados de usuário
"""

#Classe com elementos e metodos publicos
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador = +1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor

# Testando
        
conta1 = Conta('Marcus', '150.00', '15000')

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

# Como o acesso esta publico, posso ler e alterar os dados

conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 99999
conta1.limite = 9999999999

print(conta1.__dict__)


#Classe com elementos e metodos privados
class ContaSegura:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = +1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')
    
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else: 
            print('O valor dever ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 # Taxa de transferencia paga por quem realizou a transferencia

        # 2 - Adicionar o valor na conta destino
        conta_destino.__saldo += valor
        

# Testando acessos privados (forma errada)
print('\n PRIVADO')

conta2 = ContaSegura('Vinicius', 1250, 32530)

conta3 = ContaSegura('Marcus', 2000, 15000)

try:
    print(conta2._ContaSegura__numero)
    print(conta2._ContaSegura__titular)
    print(conta2._ContaSegura__saldo)
    print(conta2._ContaSegura__limite)
except AttributeError as ar:
    print(ar)
        
# Alterando dados privados (forma errada)
try:
    conta2._ContaSegura__numero = 66
    conta2._ContaSegura__titular = 'Alopramo'
    conta2._ContaSegura__saldo = 12
    conta2._ContaSegura__limite = 100
except AttributeError as ar:
    print(ar)

print(conta2.__dict__)

# Testando métodos internos

conta2.depositar(150)
print(conta2.__dict__)

conta2.sacar(300)
print(conta2.__dict__)

conta3.transferir(100, conta2)

conta2.extrato()
conta3.extrato()

