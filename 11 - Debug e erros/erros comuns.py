"""
printf('Geek University')

-- SyntaxError --

def funcao:
    print('Geek University')

-- NameError --

print(geek)

geek()

-- TypeError -- função/operação/ação aplicada a um tipo errado

print(len(5))

print('Geek' + [])

-- IndexError -- elemento em uma lista ou outro tipo de dado utilizando um indice indice invalido  

lista = ['geek']
print = [0][0]

-- ValueError -- função/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado

print(int('Geek'))

-- KeyError -- Quando acessar um dicionario com uma chave que não existe
print(dict['geek'])

-- AttributeError -- variavel não tem atributo/funcao
tupla = (11, 2, 31, 4)
print(tupla.sort())

-- IdentationError -- erro de identação (4 espaços)
def nova():
print('geek')
nova()

"""