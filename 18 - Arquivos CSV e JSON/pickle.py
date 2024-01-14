"""
Conhecendo Pikle

A função do pickle é realizar o seguinte proceso

Objeto python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

#OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma
não é recomendado trabalhar com arquivos pickle vindos de outras pessoas
que você não conheça ou de fontes desconhecidas
"""

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def mia(self):
        print(f'{self.nome} está minado...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def late(self):
        print(f'{self.nome} está latindo...')

felix = Gato('Felix')
pluto = Cachorro('Pluto')

arquivo_pickle = '18 - Arquivos CSV e JSON/animais.pickle'

with open(arquivo_pickle, 'wb') as arquivo: # wb = escrita binaria
    pickle.dump((felix, pluto), arquivo)


# leitura arquivo pickle
    
with open(arquivo_pickle, 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato._Animal__nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro._Animal__nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')