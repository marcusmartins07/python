def diz_oi():
    return 'Oi   '

alguem = 'Pedro!'

print(diz_oi() + alguem)

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

from random import random

def joga_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
    
