nome=str(input('Digite o nome completo '))

nomeSemEspaco = nome.strip()
nome = nomeSemEspaco.lower()

result = 'silva' in nome

print('Seu nome tem Silva? {}'.format(result))