nomeComp=str(input('Digite seu nome completo: ')).strip()

nomeDivido = nomeComp.split()
print('Seu primeiro nome é {}'.format(nomeDivido[0]))
print('Seu ultimo nome é {}'.format(nomeDivido[-1]))