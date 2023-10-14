cidade=str(input('Digite o nome de uma cidade: '))

cidadeSemEspaco = cidade.strip()
cidade = cidadeSemEspaco.lower()

print('santo' in cidade)