paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'Paraguai'}

print(paises['br'])

print(paises.get('br'))
print(paises.get('ru', 'Não encontrado'))

# Adcionando valor ao dicionário 
paises['ur'] = 'Argentina'
print(paises)

# Atualizando valor no dicionário
paises.update({'ur':'Uruguai'})
print(paises)

# Exluir valor do dicionário
del paises['eua']
print(paises ) 