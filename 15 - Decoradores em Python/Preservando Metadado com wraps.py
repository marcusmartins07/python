"""
Metadados = Dados intrísecos em arquivos
wraps = Funções que envolvem elementos com diversas finalidades
"""

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        # Eu sou uma função (logar) dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

def soma(a, b):
    # Soma dois numeros
    return a + b

print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)