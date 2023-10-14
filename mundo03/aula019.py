filme=dict()

filme = {
  'titulo':'Star Wars',
  'ano':1977,
  'diretor':'George Lucas'
}

print(filme)
print(filme.values())
print(filme.keys())
filme['categoria']='ficcao' #adicionando elemento
print(filme.items())

filme['diretor']='Han Solo' #substituindo

print(f'O filme {filme["titulo"]} é do {filme["diretor"]} feito em {filme["ano"]}')

for k, v in filme.items():
  print(f'O {k} é {v}')