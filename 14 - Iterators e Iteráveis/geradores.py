# Geradores = Generators = iterators

"""
Generator Function 
- Utiliza Yield = Return
- Multiplos Yield = Multiplos retornos
- Quando executa retorna um generator
"""

def conta_ate(valor_maximo):
    contador=1
    while contador <= valor_maximo:
        yield contador
        contador+=1
#obs: Generator Function gera um Generator

gen = conta_ate(5)
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen)) 