nome=str(input('Digite seu nome: '))

print(nome.upper())
print(nome.lower())

nomeSemEspaco = nome.replace(' ', '')
print(len(nomeSemEspaco))

divideNome=nome.split()
print(len(divideNome[0]))


