
# *args = paramentro padrão

# Utilizado em uma função, coloca os valores extras informados como entrada em uma tupla (tuplas são imutaveis).


def soma_todos_numeros(num1, num2, num3):
    return num1+num2+num3
print(soma_todos_numeros(4, 6, 9))

# print(soma_todos_numeros(6, 9)) TypeError
# print(soma_todos_numeros(4, 3, 6, 7)) TypeError

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(2, 3, 4, 5))

numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos_numeros(*numeros))

# O asterico serve para reconhecer que vai ser necessário desempactorar os dados

def verifica_info(*args):

    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    return 'Eu não tenho certeza de quem você é....'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))