'''
Default Dict - Usamos para informar uma informação padrão, caso tente acessar
uma chave que não existe, essa chave será criada e o valor default será atribuido

OBS: Lambda = Funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores
'''

from collections import defaultdict

dicionario = defaultdict(lambda : 0)

dicionario['curso'] = 'Programação em Python'

print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])
print(dicionario)