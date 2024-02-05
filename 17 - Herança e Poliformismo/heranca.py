"""
POO - Herança (Inheritance)

A ideia de heranca é a de reaproveitar código. Também extender nossas classes

Com uma classe existente, nós extendemos outra classe que passa
a herdar atributos e métodos da classe herdada

Sempre se perguntar se existe alguma entidade genérica o suficiente para
encapsular os atributos e métodos comuns a outras entidades?

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
Class Pessoa = Super Classe; classe mãe; classe pai, classe base, classe generica

Quando uma classe herda de otura classe, ela é chamada:
class cliente ou funcionario = sun classe; classe filha; classe especifica
"""

class Pessoa:
    def __init__ (self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
class Cliente(Pessoa):
    #Cliente herda de pessoa
    def __init__ (self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda
    
class Funcionario(Pessoa):
    #Funcionario herda de pessoa
    def __init__ (self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
    
    # Sobrescrita de metódos (Overriding)
    def nome_completo(self):
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'
         

cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-80', 50000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-21', 2345)

print(cliente1.__dict__)
print(funcionario1.__dict__)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

