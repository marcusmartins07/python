"""
Poo - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Quando reimplementamos um metodo presente na classe pai em clsses filhas estamos realizando uma sobrescrita de método (overrinding)

Overriding é a melgor representação de polimorfismo
"""

class Animal(object): #Todas classe herda "object" logo esta forma e redundante
    
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método') # rasie é uma exeção
    
    def comer(self):
        print(f'{self.__nome} esta comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')
    

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau!')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo!')

# Testes
        
felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()