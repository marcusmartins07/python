"""
Funções de maior grandeza - Higher Order Functions

Podemos ter funções que retornam outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras funções,
até mesmo criar variáveis do tipo de funções nos nossos programas
"""

# Exemplo

def somar (a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando função
print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

"""
Nested Functions - Funções Aninhadas

Podemos ter funções dentro de funções, que são conhecidas por Nested Functions,
ou tambpem Inner Functions (funções internas)
"""

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai  ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

#testando

print(cumprimento('Angelina'))
print(cumprimento('Felicity'))