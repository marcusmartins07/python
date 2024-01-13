"""
Herança Multipla = Classe que herda de multiplas classes fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

#Obs: A Heranã multipla pode ser feitasde duas maneiras
 - Multiderivação direta
 - Multiderivação indireta

 Indenpendente se a derivação for direta ou indireta. A classe herdará todos os atributos das super classes

"""

# Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    pass


# Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass 

 