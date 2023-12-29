def mostra_informacao(nome='Geek', Instrutor=False):
    if nome == 'Geek' and Instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(Instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Evitar variaveis globais
total = 0

def incrementa():
    global total

    total = total +1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

# Função com função interna

def fora():
    contador = 0
    
    def dentro():
        nonlocal contador # esta puxando a varavel de fora da função, logo toda vez que executada ela começa com zero

        contador +=1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

#print(dentro()) #NameError
